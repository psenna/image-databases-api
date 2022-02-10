from typing import List, Optional
from pydantic import BaseModel


class DatasetUpdateRequest(BaseModel):
    name: Optional[str]

class DatasetCreateRequest(BaseModel):
    name: str

class DatasetResponse(BaseModel):
    id: int
    name: Optional[str]

class DatasetPage(BaseModel):
    items: List[DatasetResponse]
    total: int
    page_size: int
    page: int