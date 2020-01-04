import os

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