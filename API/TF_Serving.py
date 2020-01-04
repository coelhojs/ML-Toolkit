import json

import numpy as np
import requests

import utils


class TF_Serving: 
    Headers = {"content-type": "application/json"}
    Images = []
    Labels = []
    Url = ""


    # default constructor 
    def __init__(self, url, images, labels): 
        self.Images = images
        self.Labels = labels
        self.Url = url


    def call_img_classification(self):
        print(f'\n\nMaking request to {self.Url}...\n')
        for image_path in self.Images:
            # Converte o arquivo num float array
            formatted_json_input = utils.classification_pre_process(image_path)
            server_response = requests.post(self.Url, data=formatted_json_input, headers=self.Headers)
            print(server_response)

            # Decoding results from TensorFlow Serving server
            pred = json.loads(server_response.content.decode('utf-8'))
            predictions = np.squeeze(pred['predictions'][0])
            results = []
            top_k = predictions.argsort()[-5:][::-1]
            labels = self.Labels
            for i in top_k:
                label = labels[i]
                score = float(predictions[i])
                results.append('{label},{score}'.format(label=label,score=score))
        print(f'Request returned\n')
        return results
