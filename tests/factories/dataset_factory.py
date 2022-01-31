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