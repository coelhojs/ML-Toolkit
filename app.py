import json

import config
from flask import Flask, jsonify, request, url_for
from waitress import serve
from Image_Classification import Image_Classification
from Object_Detection import Object_Detection
from Response import Response
from Retrainer import Retrainer

app = Flask(__name__)


@app.route('/vera_species/classify/', methods=['POST'])
def vera_species_classify():
    try:
        response = Response(
            request.json['Id'], request.json['Method'], request.json['Model'])

        species_classification = Image_Classification(
            request.json['Images'], request.json['Model'], config.vera_species, request.remote_addr)

        results = species_classification.classification_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)

    except Exception as error:
        raise error


@app.route('/vera_poles_trees/detect/', methods=['POST'])
def vera_poles_trees_detect():
    try:
        response = Response(
            request.json['Id'], request.json['Method'], request.json['Model'])

        object_detection = Object_Detection(
            request.json['Images'], request.json['Model'], config.vera_poles_trees, request.remote_addr)

        results = object_detection.detection_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)

    except Exception as error:
        raise error


@app.route('/vera_species/retrain/', methods=['POST'])
def vera_species_retrain():
    try:
        response = Response(request.json['Id'], request.json['Method'], request.json['Model'])

        retraining = Retrainer(request.json['Workspace'], request.json['Steps'])

        results = retraining.image_classification_retrainer()

        response.set_results(results)

        return json.dumps(response.__dict__)

    except Exception as error:
        raise error

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
#     #app.run(host='0.0.0.0', threaded=True)
if __name__ == "__main__":
   #app.run() ##Replaced with below code to run it using waitress 
   serve(app, host='0.0.0.0', port=8000)
