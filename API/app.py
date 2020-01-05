import json

from celery import Celery
from flask import Flask, jsonify, request

from Image_Classification import Image_Classification
from Object_Detection import Object_Detection
from Response import Response

app = Flask(__name__)
app.config.from_object("config")

client = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
client.conf.update(app.config)


@app.route('/vera_species/classify/', methods=['POST'])
def vera_species_classify():
    try:
        response = Response(request.json['Id'], request.json['Method'], request.json['Model'])

        species_classification = Image_Classification(request.json['Images'], request.json['Model'], app.config['vera_species'], request.remote_addr)

        results = species_classification.classification_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)
        
    except Exception as error:
        raise error


@app.route('/vera_poles_trees/detect/', methods=['POST'])
def vera_poles_trees_detect():
    try:
        response = Response(request.json['Id'], request.json['Method'], request.json['Model'])

        object_detection = Object_Detection(request.json['Images'], request.json['Model'], app.config['vera_poles_trees'], request.remote_addr)

        results = object_detection.detection_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)
        
    except Exception as error:
        raise error


# @app.route('/vera_species/retrain/', methods=['POST'])
# def vera_species_retrain():
#     try:
#         response = Response(request.json['Id'], request.json['Method'], request.json['Model'])

#         species_classification = Image_Classification(request.json['Images'], request.json['Model'], app.config['vera_species'])

#         results = species_classification.classification_caller()

#         response.set_results(results)

#         return json.dumps(response.__dict__)
        
#     except Exception as error:
#         raise error
