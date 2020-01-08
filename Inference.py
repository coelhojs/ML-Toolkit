import numpy as np
import tensorflow as tf
from PIL import Image

from utils import img_utils
from utils import ops as utils_ops

#Configuracoes de otimizacao
config = tf.compat.v1.ConfigProto(allow_soft_placement=True,
                                intra_op_parallelism_threads=0, 
                                inter_op_parallelism_threads=0)

class Inference:
    Graph: ""
    Labels: ""


    def __init__(self, config, method): 
        self.Method = method
        self.Graph = self.load_graph(config['graph'], self.Method)
        self.Labels = self.load_labels(config['label_map'])


    def image_classifier(self, images_list, input_layer = "Placeholder", output_layer = "final_result"):
        input_height = 299
        input_width = 299
        input_mean = 0
        input_std = 255
        response = []
        for image_path in images_list:
            t = self.read_tensor_from_image_file(
                image_path,
                input_height=input_height,
                input_width=input_width,
                input_mean=input_mean,
                input_std=input_std)

            input_name = "import/" + input_layer
            output_name = "import/" + output_layer
            input_operation = self.Graph.get_operation_by_name(input_name)
            output_operation = self.Graph.get_operation_by_name(output_name)

            with tf.compat.v1.Session(config=config, graph=self.Graph) as sess:
                inference = sess.run(output_operation.outputs[0], {
                    input_operation.outputs[0]: t
                })
            inference = np.squeeze(inference)
            results = []
            top_k = inference.argsort()[-5:][::-1]
            for i in top_k:
                label = self.Labels[i]
                score = float(inference[i])
                results.append('{label},{score}'.format(label=label,score=score))

            response.append(results)
            
        return response


    def objects_detector(self, images_list):
        response = []
        for image_path in images_list:
            inference = self.run_inference_for_single_image(self.Graph, image_path, self.Labels)

            response.append(inference)

        return response

    def load_graph(self, model_path, method):
        if (method=="image_classification"):
            return self.load_classification_graph(model_path)
        elif (method=="object_detection"):
            return self.load_detection_graph(model_path)

    def load_classification_graph(self, model_path):
        graph = tf.Graph()
        graph_def = tf.compat.v1.GraphDef()

        with open(model_path, "rb") as f:
            graph_def.ParseFromString(f.read())
        with graph.as_default():
            tf.import_graph_def(graph_def)

        return graph

    def load_detection_graph(self, model_path):
        graph = tf.Graph()
        with graph.as_default():
            od_graph_def = tf.compat.v1.GraphDef()
            with tf.io.gfile.GFile(model_path, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        return graph



    def load_labels(self, label_file):
        label = []
        proto_as_ascii_lines = tf.io.gfile.GFile(label_file).readlines()
        for l in proto_as_ascii_lines:
            label.append(l.rstrip())
        return label


    def read_tensor_from_image_file(self, image_path,
                                    input_height=299,
                                    input_width=299,
                                    input_mean=0,
                                    input_std=255):
        input_name = "file_reader"
        output_name = "normalized"
        file_reader = tf.io.read_file(image_path, input_name)
        if image_path.endswith(".png"):
            image_reader = tf.image.decode_png(
                file_reader, channels=3, name="png_reader")
        elif image_path.endswith(".gif"):
            image_reader = tf.squeeze(
                tf.image.decode_gif(file_reader, name="gif_reader"))
        elif image_path.endswith(".bmp"):
            image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
        else:
            image_reader = tf.image.decode_jpeg(
                file_reader, channels=3, name="jpeg_reader")

        float_caster = tf.cast(image_reader, tf.float32)
        dims_expander = tf.expand_dims(float_caster, 0)
        resized = tf.compat.v1.image.resize_bilinear(dims_expander, [input_height, input_width])
        normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
        sess = tf.compat.v1.Session(config=config)
        result = sess.run(normalized)

        return result


    def run_inference_for_single_image(self, graph, image_path, labels):
        with graph.as_default():
            with tf.compat.v1.Session(config=config) as sess:
                try:
                    image = Image.open(image_path).convert("RGB")
                except:
                    raise Exception('Imagem {image_path} nao localizada.'.format(image_path=image_path))

                # Get handles to input and output tensors
                ops = tf.compat.v1.get_default_graph().get_operations()
                all_tensor_names = {
                    output.name for op in ops for output in op.outputs}
                tensor_dict = {}
                for key in [
                    'num_detections', 'detection_boxes', 'detection_scores',
                    'detection_classes', 'detection_masks'
                ]:
                    tensor_name = key + ':0'
                    if tensor_name in all_tensor_names:
                        tensor_dict[key] = tf.compat.v1.get_default_graph().get_tensor_by_name(
                            tensor_name)
                if 'detection_masks' in tensor_dict:
                    # The following processing is only for single image
                    detection_boxes = tf.squeeze(
                        tensor_dict['detection_boxes'], [0])
                    detection_masks = tf.squeeze(
                        tensor_dict['detection_masks'], [0])
                    # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
                    real_num_detection = tf.cast(
                        tensor_dict['num_detections'][0], tf.int32)
                    detection_boxes = tf.slice(detection_boxes, [0, 0], [
                                                real_num_detection, -1])
                    detection_masks = tf.slice(detection_masks, [0, 0, 0], [
                                                real_num_detection, -1, -1])
                    detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                        detection_masks, detection_boxes, image.shape[0], image.shape[1])
                    detection_masks_reframed = tf.cast(
                        tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                    # Follow the convention by adding back the batch dimension
                    tensor_dict['detection_masks'] = tf.expand_dims(
                        detection_masks_reframed, 0)
                image_tensor = tf.compat.v1.get_default_graph().get_tensor_by_name('image_tensor:0')
                image_np = img_utils.load_image_into_numpy_array(image)

                # Run inference
                output_dict = sess.run(tensor_dict,
                                        feed_dict={image_tensor: np.expand_dims(image_np, 0)})
                # all outputs are float32 numpy arrays, so convert types as appropriate
                output_dict['num_detections'] = int(
                    output_dict['num_detections'][0])
                output_dict['detection_classes'] = output_dict[
                    'detection_classes'][0].astype(np.uint8)
                output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
                output_dict['detection_scores'] = output_dict['detection_scores'][0]
                if 'detection_masks' in output_dict:
                    output_dict['detection_masks'] = output_dict['detection_masks'][0]

                output_dict = img_utils.post_process(output_dict, image_path, labels)

        return output_dict
