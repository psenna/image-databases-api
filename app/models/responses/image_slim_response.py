from typing import Optional
from pydantic import BaseModel

from app.models.responses.dataset_response import DatasetResponse


class ImageSlimResponse(BaseModel):
    """Image response without the image data"""
    name: str
    thumbnail: bytes
    dataset: Optional[DatasetResponse]