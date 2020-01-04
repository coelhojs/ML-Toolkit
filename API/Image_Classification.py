import requests

import config
import utils
from Inference import Inference
from TF_Serving import TF_Serving


class Image_Classification:
    Config = ""
    Images: []
    Model: ""
    Url: ""
    User: ""

    def __init__(self, images, model, config): 
        self.Images = images
        self.Model = model
        self.Config = config


    def classification_caller(self):
        try:
            #TF-Serving test_request
            requests.get(self.Config['test_url'])

            print("Utilizando Tensorflow Serving para classificação.")

            prediction = TF_Serving(self.Config['serving_url'], self.Images, utils.load_labels(self.Config['label_map']))

            return prediction.call_img_classification()

        except:
            print("Tensorflow Serving não detectado. Utilizando scripts locais")
                        
            inference = Inference(self.Config)

            return inference.image_classifier(self.Images)
