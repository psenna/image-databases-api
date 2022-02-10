from typing import Dict
from app.models.label import Label


class LabelFactory():
    @classmethod
    def get_valid_properties(cls, props:Dict = {}):
        default_props = {
            "id": 0,
            "name": "label123",
        }

        return default_props | props

    @classmethod
    def get_valid_request(cls, props:Dict = {}):
        return cls.get_valid_properties(props=props)
    
    @classmethod
    async def create(cls, props:Dict = {}) -> Label:
        new_label = Label(**cls.get_valid_properties(props=props))
        await new_label.save()
        return new_label
