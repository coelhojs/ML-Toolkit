from Inference import Inference
from utils import img_utils


class Object_Detection:
    Config = ""
    Images: []
    Model: ""

    def __init__(self, images, model, config, remote_addr):
        self.Images = img_utils.validate_paths(images, remote_addr)
        self.Model = model
        self.Config = config

    def detection_caller(self):
        try:
            inference = Inference(self.Config, "object_detection")

            return inference.objects_detector(self.Images)

        except Exception as error:
            raise error
