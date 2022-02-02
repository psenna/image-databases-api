from typing import List
from pydantic import BaseModel

from app.models.responses.dataset_response import DatasetResponse


class DatasetPage(BaseModel):
    items: List[DatasetResponse]
    total: int
    page_size: int
    page: int