from typing import List, Optional
from pydantic import BaseModel
from app.models.responses.label_response import LabelResponse
from app.models.responses.dataset_response import DatasetResponse


class ImageFullResponse(BaseModel):
    """Image full response with all image data"""
    name: str
    thumbnail: bytes
    data: bytes
    dataset: Optional[DatasetResponse]
    labels: List[LabelResponse]