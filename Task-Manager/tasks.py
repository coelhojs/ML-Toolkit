import json
import os
import time

from celery import Celery

from Image_Classification import Image_Classification
from Object_Detection import Object_Detection
from Response import Response

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.vera_species_classify')
def vera_species_classify(request, config):
    try:
        response = Response(request.json['Id'], request.json['Method'], request.json['Model'])

        species_classification = Image_Classification(request.json['Images'], request.json['Model'], config, request.remote_addr)

        results = species_classification.classification_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)
        
    except Exception as error:
        raise error

@celery.task(name='tasks.vera_poles_trees_detect')
def vera_poles_trees_detect():
    try:
        response = Response(request.json['Id'], request.json['Method'], request.json['Model'])

        object_detection = Object_Detection(request.json['Images'], request.json['Model'], app.config['vera_poles_trees'], request.remote_addr)

        results = object_detection.detection_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)
        
    except Exception as error:
        raise error


# @celery.task(name='tasks.vera_species_retrain')
# def vera_species_retrain():
#     try:
#         response = Response(request.json['Id'], request.json['Method'], request.json['Model'])

#         species_classification = Image_Classification(request.json['Images'], request.json['Model'], app.config['vera_species'])

#         results = species_classification.classification_caller()

#         response.set_results(results)

#         return json.dumps(response.__dict__)
        
#     except Exception as error:
#         raise error
