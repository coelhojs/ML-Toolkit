from Inference import Inference
from utils import img_utils


class Image_Classification:
    Config = ""
    Images: []
    Model: ""

    def __init__(self, images, config, remote_addr):
        self.Images = img_utils.validate_paths(images, remote_addr)
        self.Config = config

    def classification_caller(self):
        try:
            inference = Inference(self.Config, "image_classification")
            #TODO: Tornar assíncrono neste ponto
            return inference.image_classifier(self.Images)

        except Exception as error:
            raise error
