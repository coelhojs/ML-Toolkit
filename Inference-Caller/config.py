import os

vera_species = {
    'graph': '{ROOT}/models/vera_species/1/retrained_graph.pb'.format(ROOT=os.getcwd()),
    'label_map': '{ROOT}/models/vera_species/vera_species_labels.txt'.format(ROOT=os.getcwd())
}