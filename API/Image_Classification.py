import config
import requests

class Image_Classification:
    Images: []
    Model: ""
    User: ""

    # default constructor 
	def __init__(images, model): 
		self.Images = images
        self.Model = model


    def species_classifier():
    # TODO: Utilizar try/catch para registro de logs e garantir que as requisições vieram parametrizadas corretamente
    #Tenta conexão com Tensorflow Serving, se não conseguir conectar, usar script local:
    try:
        #test_request
        requests.get(config.vera_species['test_url'])

        print("Tensorflow Serving detectado. Utilizando para classificação")

        prediction = TF_Serving(config.vera_species['prediction_url'], self.Images)

        return prediction.call_img_classification()

    except:
        print("Tensorflow Serving não detectado. Utilizando scripts locais")
        #Alterar essa chamada para usar docker
        response.Results = image_classifier(request.json['Images'], model_path, label_file)

    # Returning JSON response to the frontend
    return jsonify(response)
