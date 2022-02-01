import base64
import os

from app.utils.image_utils import get_b64thumbnail_from_b64image

class ImageFactory():
    @classmethod
    def get_valid_dataset_properties(cls, dataset_id: int):
        properties =  cls.get_valid_dataset_request(dataset_id)
        properties['thumbnail'] = get_b64thumbnail_from_b64image(properties['data'])
        return properties


    @classmethod
    def get_valid_dataset_request(cls, dataset_id: int):
        return {
            "id": 0,
            "name": "image.png",
            "dataset": dataset_id,
            "data": cls.get_b64_image()
        }


    @classmethod
    def get_b64_image(cls):
        dirname = os.path.dirname(__file__)
        with open(f"{dirname}/sample_data/tela.png", "rb") as f:
            image_data = base64.b64encode(f.read()).decode('ascii')
            return image_data