from typing import List
from pydantic import BaseModel

from app.models.responses.label_response import LabelResponse


class LabelPage(BaseModel):
    items: List[LabelResponse]
    total: int
    page_size: int
    page: int