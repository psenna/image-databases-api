from app.models.dataset import Dataset


class DatasetFactory():
    @classmethod
    def get_valid_dataset_properties(cls):
        return {
            "id": 0,
            "name": "Dataset123",
        }

    @classmethod
    def get_valid_dataset_request(cls):
        return cls.get_valid_dataset_properties()
    
    @classmethod
    async def create_dataset(cls) -> Dataset:
        new_dataset = Dataset(**cls.get_valid_dataset_properties())
        await new_dataset.save()
        return new_dataset
