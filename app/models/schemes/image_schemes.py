from typing import List, Optional
from pydantic import BaseModel, Field, root_validator
from fastapi import HTTPException
import PIL

from app.models.schemes.label_schemes import LabelResponse
from app.models.schemes.dataset_schemes import DatasetResponse
from app.utils.image_utils import get_b64thumbnail_from_b64image


class ImageCreateRequest(BaseModel):
    name: str
    data: bytes
    dataset: int
    thumbnail: Optional[bytes] = Field(alias="thumbnail")

    @root_validator(pre=True)
    def create_thumbnail(cls, values):
        image = values['data']
        try:
            values['thumbnail'] = get_b64thumbnail_from_b64image(image)
        except PIL.UnidentifiedImageError:
            raise HTTPException(status_code=400, detail="The data is not a valid image!")
        return values

class ImageSlimResponse(BaseModel):
    """Image response without the image data"""
    id: int
    name: str
    thumbnail: bytes
    dataset: Optional[DatasetResponse]
    labels: List[LabelResponse]

class ImageFullResponse(BaseModel):
    """Image full response with all image data"""
    name: str
    thumbnail: bytes
    data: bytes
    dataset: Optional[DatasetResponse]
    labels: List[LabelResponse]

class ImagePage(BaseModel):
    items: List[ImageSlimResponse]
    total: int
    page_size: int
    page: int