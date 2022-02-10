import base64
import os
from typing import Dict
from app.models.image import Image
from app.utils.image_utils import get_b64thumbnail_from_b64image

class ImageFactory():
    @classmethod
    def get_valid_properties(cls, dataset_id: int, props:Dict = {}):
        properties =  cls.get_valid_request(dataset_id, props=props)
        properties['thumbnail'] = get_b64thumbnail_from_b64image(properties['data'])
        return properties


    @classmethod
    def get_valid_request(cls, dataset_id: int, props:Dict = {}):
        default_props = {
            "id": 0,
            "name": "image.png",
            "dataset": dataset_id,
            "data": cls.get_b64_image()
        }
        return default_props | props

    @classmethod
    async def create(cls, dataset_id: int, props:Dict = {}) -> Image:
        new_image = Image(**cls.get_valid_properties(dataset_id, props=props))
        await new_image.save()
        return new_image


    @classmethod
    def get_b64_image(cls):
        dirname = os.path.dirname(__file__)
        with open(f"{dirname}/sample_data/tela.png", "rb") as f:
            image_data = base64.b64encode(f.read()).decode('ascii')
            return image_data

    @classmethod
    def get_b64_text(cls):
        dirname = os.path.dirname(__file__)
        with open(f"{dirname}/sample_data/not_image.txt", "rb") as f:
            image_data = base64.b64encode(f.read()).decode('ascii')
            return image_data