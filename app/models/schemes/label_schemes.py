from typing import List, Optional
from pydantic import BaseModel

class LabelCreateRequest(BaseModel):
    name: str

class LabelUpdateRequest(BaseModel):
    name: str

class LabelResponse(BaseModel):
    id: Optional[int]
    name: Optional[str]


class LabelPage(BaseModel):
    items: List[LabelResponse]
    total: int
    page_size: int
    page: int