from typing import Optional
from pydantic import BaseModel

from app.models.responses.dataset_response import DatasetResponse


class ImageFullResponse(BaseModel):
    """Image full response with all image data"""
    name: str
    thumbnail: bytes
    data: bytes
    dataset: Optional[DatasetResponse]