from app.models.label import Label


class LabelFactory():
    @classmethod
    def get_valid_properties(cls):
        return {
            "id": 0,
            "name": "label123",
        }

    @classmethod
    def get_valid_request(cls):
        return cls.get_valid_properties()
    
    @classmethod
    async def create(cls) -> Label:
        new_label = Label(**cls.get_valid_properties())
        await new_label.save()
        return new_label
