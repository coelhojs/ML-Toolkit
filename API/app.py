import json

import celery.states as states
import config
from celery import Celery
from flask import Flask, jsonify, request, url_for
from worker import celery

app = Flask(__name__)

@app.route('/vera_species/classify/', methods=['POST'])
def vera_species_classify():
    try:    
        task = celery.send_task('tasks.vera_species_classify', args=[request, config['vera_species']], kwargs={})
        response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
        return response
    except Exception as error:
        raise error


@app.route('/vera_poles_trees/detect/', methods=['POST'])
def vera_poles_trees_detect():
    try:    
        task = celery.send_task('tasks.vera_poles_trees_detect', args=[request, config['vera_poles_trees']], kwargs={})
        response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
        return response
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
