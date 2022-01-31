from pydantic import BaseModel


class DatasetUpdateRequest(BaseModel):
    name: str