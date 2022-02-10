from typing import Dict
from app.models.dataset import Dataset


class DatasetFactory():
    @classmethod
    def get_valid_properties(cls, props:Dict = {}):
        default_props = {
            "id": 0,
            "name": "Dataset123",
        }

        return default_props | props

    @classmethod
    def get_valid_dataset_request(cls, props:Dict = {}):
        return cls.get_valid_properties(props=props)
    
    @classmethod
    async def create(cls, props:Dict = {}) -> Dataset:
        new_dataset = Dataset(**cls.get_valid_properties(props=props))
        await new_dataset.save()
        return new_dataset
