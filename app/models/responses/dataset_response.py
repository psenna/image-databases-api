from pydantic import BaseModel


class DatasetResponse(BaseModel):
    id: int
    name: str