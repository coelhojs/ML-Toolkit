import os

vera_species = {
    'label_map': '{ROOT}/models/vera_species_labels.txt'.format(ROOT=os.getcwd()),
    'inference_url': "http://localhost:8502/v1/models/vera_species:predict",
    'serving_url': "http://localhost:8501/v1/models/vera_species:predict",
    'test_url': "http://localhost:8501/v1/models/vera_species"
}