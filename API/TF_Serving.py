import json

import numpy as np
import requests

from utils import img_utils


class TF_Serving: 
    Headers = {"content-type": "application/json"}
    Images = []
    Labels = []
    Results = []
    Url = ""

    def __init__(self, url, images, labels): 
        self.Images = images
        self.Labels = labels
        self.Url = url


    def call_img_classification(self):
        print(f'\n\nMaking request to {self.Url}...\n')
        for image_path in self.Images:
            # Converte o arquivo num float array
            formatted_json_input = img_utils.pre_process(image_path)
            server_response = requests.post(self.Url, data=formatted_json_input, headers=self.Headers)
            print(server_response)

            # Decoding results from TensorFlow Serving server
            pred = json.loads(server_response.content.decode('utf-8'))
            predictions = np.squeeze(pred['predictions'][0])
            top_k = predictions.argsort()[-5:][::-1]
            labels = self.Labels
            for i in top_k:
                label = labels[i]
                score = float(predictions[i])
                self.Results.append('{label},{score}'.format(label=label,score=score))
        print(f'Request returned\n')
        return self.Results


    def call_obj_detection(self):
        print(f'\n\nMaking request to {self.Url}...\n')
        for image_path in self.Images:
            # Converte o arquivo num float array
            formatted_json_input = img_utils.pre_process(image_path)
            server_response = requests.post(self.Url, data=formatted_json_input, headers=self.Headers)
            print(server_response)

            #Post proccess
            self.Results.append(img_utils.post_process(server_response, image_path, self.Labels))
        return self.Results
