import requests

import config
from utils import img_utils
from Inference import Inference
from TF_Serving import TF_Serving


class Object_Detection:
    Config = ""
    Images: []
    Model: ""

    def __init__(self, images, model, config, remote_addr): 
        self.Images = img_utils.validate_paths(images, remote_addr)
        self.Model = model
        self.Config = config


    def detection_caller(self):
        try:
            #TF-Serving test_request
            requests.get(self.Config['test_url'])

            print("Utilizando Tensorflow Serving para detecção.")

            prediction = TF_Serving(self.Config['serving_url'], self.Images, img_utils.load_labels(self.Config['label_map']))

            return prediction.call_obj_detection()

        except:
            print("Tensorflow Serving não detectado. Utilizando scripts locais")
                        
            inference = Inference(self.Config)

            return inference.objects_detector(self.Images)
