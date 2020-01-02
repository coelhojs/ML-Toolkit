import json
from Image_Classification import Image_Classification
from Response import Response
from flask import Flask, jsonify, request
import config
app = Flask(__name__)

@app.route('/vera_species/classify/', methods=['POST'])
def vera_species_classify():
    try:
        response = Response(request.json['Id'], request.json['Method'], request.json['Model'])

        species_classification = Image_Classification(request.json['Images'], request.json['Model'], config.vera_species)

        results = species_classification.classification_caller()

        response.set_results(results)

        return json.dumps(response.__dict__)
        
    except Exception as error:
        raise error
