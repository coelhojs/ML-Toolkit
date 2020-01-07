# Métodos utilitários utilizados na classificação de images e detecção de objetos
import json

import numpy as np
import tensorflow as tf
from PIL import Image


def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.io.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label.append(l.rstrip())
    return label


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


def pre_process(image_path):
    try:
        image = Image.open(image_path).convert("RGB")

        image_np = load_image_into_numpy_array(image)

        # Expand dims to create  bach of size 1
        image_tensor = np.expand_dims(image_np, 0)
        formatted_json_input = json.dumps({
            "signature_name": "serving_default",
            "instances": image_tensor.tolist()
        })

        return formatted_json_input

    except:
        raise Exception('Imagem {image_path} nao localizada.'.format(image_path=image_path))


def post_process(server_response, image_path, labels):

    image = Image.open(image_path).convert("RGB")
    image_np = load_image_into_numpy_array(image)

    #TODO: Verificar essa lógica!
    try:
        response = json.loads(server_response.text)
        output_dict = response['predictions'][0]
    except:
        output_dict = server_response

    # all outputs are float32 numpy arrays, so convert types as appropriate
    filtered_scores = list(
        filter(lambda x: (x > 0.5), output_dict['detection_scores']))
    output_dict['detection_scores'] = filtered_scores
    output_dict['num_detections'] = int(len(output_dict['detection_scores']))
    filtered_classes = output_dict['detection_classes'][0:output_dict['num_detections']]

    named_classes = list(map(lambda x: labels[int(x)-1], filtered_classes))
    output_dict['detection_classes'] = named_classes
    filtered_boxes = output_dict['detection_boxes'][0:output_dict['num_detections']]
    output_dict['detection_boxes'] = filtered_boxes

    # Formatando resultado para o modelo esperado pelo Vera
    inference_dict = {}
    inference_dict['ImagePath'] = image_path
    inference_dict['Class'] = output_dict['detection_classes']
    inference_dict['BoundingBoxes'] = output_dict['detection_boxes'].tolist()
    inference_dict['Score'] = np.array(output_dict['detection_scores']).tolist()
    inference_dict['NumDetections'] = output_dict['num_detections']

    return inference_dict


def validate_paths(images, remote_addr):
    newList = []
    for imagepath in images:
        if ("C:" in imagepath):
            newPath = imagepath.replace(
                "C:/", "//{remote_addr}/c/".format(remote_addr=remote_addr))
            newList.append(newPath)
        elif ("c:" in imagepath):
            newPath = imagepath.replace(
                "c:/", "//{remote_addr}/c/".format(remote_addr=remote_addr))
            newList.append(newPath)
        else:
            newList.append(imagepath)
    return newList