import json
import os
import time

import config
from celery import Celery
from Image_Classification import Image_Classification
from Object_Detection import Object_Detection
from Response import Response

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.vera_species_classify')
def vera_species_classify(request, sender):
    try:
        response = Response(request['Id'], request['Method'], request['Model'])

        species_classification = Image_Classification(request['Images'], request['Model'], config.vera_species, sender)

        results = species_classification.classification_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)
        
    except Exception as error:
        raise error

@celery.task(name='tasks.vera_poles_trees_detect')
def vera_poles_trees_detect(request, sender):
    try:
        response = Response(request['Id'], request['Method'], request['Model'])

        object_detection = Object_Detection(request['Images'], request['Model'], config.vera_poles_trees, sender)

        results = object_detection.detection_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)
        
    except Exception as error:
        raise error


# @celery.task(name='tasks.vera_species_retrain')
# def vera_species_retrain():
#     try:
#         response = Response(request['Id'], request['Method'], request['Model'])

#         species_classification = Image_Classification(request['Images'], request['Model'], app.config['vera_species'])

#         results = species_classification.classification_caller()

#         response.set_results(results)

#         return json.dumps(response.__dict__)
        
#     except Exception as error:
#         raise error
