import os

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

vera_species = {
    'label_map': '{ROOT}/models/vera_species/label_map.txt'.format(ROOT=os.getcwd()),
    'graph': '{ROOT}/models/vera_species/1/retrained_graph.pb'.format(ROOT=os.getcwd()),
    'serving_url': "http://tf-serving:8501/v1/models/vera_species:predict",
    'test_url': "http://tf-serving:8501/v1/models/vera_species"
}
# vera_species = {
#     'label_map': '{ROOT}/models/vera_species_labels.txt'.format(ROOT=os.getcwd()),
#     'inference_url': "http://localhost:8502/v1/models/vera_species:predict",
#     'serving_url': "http://localhost:8501/v1/models/vera_species:predict",
#     'test_url': "http://localhost:8501/v1/models/vera_species"
# }
vera_poles_trees = {
    'label_map': '{ROOT}/models/vera_poles_trees/label_map.pbtxt'.format(ROOT=os.getcwd()),
    'graph': '{ROOT}/models/vera_poles_trees/1/frozen_inference_graph.pb'.format(ROOT=os.getcwd()),
    'serving_url': "http://tf-serving:8501/v1/models/vera_poles_trees:predict",
    'test_url': "http://tf-serving:8501/v1/models/vera_poles_trees"
}