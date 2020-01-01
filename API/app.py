import base64
import json
import os
import time
from io import BytesIO
from os import listdir
from os.path import isfile, join

import Image_Classification, Response
import numpy as np
import requests
from flask import Flask, jsonify, request
from PIL import Image
from tensorflow.contrib import util as contrib_util
from tensorflow.keras.applications import inception_v3
from tensorflow.keras.preprocessing import image

from object_detection_caller import (object_detection_batch_script,
                                     object_detection_batch_serving)
from tensorflow_scripts.image_classification.label_image import \
    image_classifier
from tensorflow_scripts.object_detection.object_detection import \
    objects_detector
from tensorflow_scripts.utils import img_util, label_map_util
from tensorflow_scripts.utils.label_util import load_labels

app = Flask(__name__)

@app.route('/vera_species/classify/', methods=['POST'])
def vera_species_classify():
    try:
        response = Response(request.json['Id'], "Species_classification")

        species_classification = Image_Classification(request.json['Images'], "vera_species")

        results = species_classification.species_classifier()

        response.set_results(results)

        return response
        
    except:
        return "Houve um erro."