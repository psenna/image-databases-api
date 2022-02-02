from typing import List, Optional
from pydantic import BaseModel
from app.models.responses.label_response import LabelResponse
from app.models.responses.dataset_response import DatasetResponse


class ImageSlimResponse(BaseModel):
    """Image response without the image data"""
    name: str
    thumbnail: bytes
    dataset: Optional[DatasetResponse]
    labels: List[LabelResponse]