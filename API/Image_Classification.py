import config
import requests

class Image_Classification:
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
            requests.get(self.config['test_url'])

            print("Utilizando Tensorflow Serving para classificação.")

            prediction = TF_Serving(self.config['serving_url'], self.Images, utils.load_labels(self.config['label_map']))

            return prediction.call_img_classification()

        except:
            print("Tensorflow Serving não detectado. Utilizando scripts locais")
            
            #Alterar essa chamada para usar docker
            # response.Results = image_classifier(self.Images, model_path, label_file)

            # Returning JSON response to the frontend
            # return jsonify(response)