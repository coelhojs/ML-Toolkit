import os

vera_species = {
    'label_map': '{ROOT}/models/vera_species/label_map.txt'.format(ROOT=os.getcwd()),
    'graph': '{ROOT}/models/vera_species/1/retrained_graph.pb'.format(ROOT=os.getcwd())
}
vera_poles_trees = {
    'label_map': '{ROOT}/models/vera_poles_trees/label_map.pbtxt'.format(ROOT=os.getcwd()),
    'graph': '{ROOT}/models/vera_poles_trees/1/frozen_inference_graph.pb'.format(ROOT=os.getcwd())
}