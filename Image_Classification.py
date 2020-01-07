from Inference import Inference
from utils import img_utils


class Image_Classification:
    Config = ""
    Images: []
    Model: ""

    def __init__(self, images, model, config, remote_addr):
        self.Images = img_utils.validate_paths(images, remote_addr)
        self.Model = model
        self.Config = config

    def classification_caller(self):
        try:
            inference = Inference(self.Config, "image_classification")

            return inference.image_classifier(self.Images)

        except Exception as error:
            raise error
