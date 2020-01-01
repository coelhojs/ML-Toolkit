import os

vera_species = {
    'test_url': "http://localhost:8501/v1/models/vera_species",
    'prediction_url': "http://localhost:8501/v1/models/vera_species:predict",
    'label_map': '{ROOT}/models/vera_species_labels.txt'.format(ROOT=os.getcwd())
}