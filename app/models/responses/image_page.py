from typing import List
from pydantic import BaseModel

from app.models.responses.image_slim_response import ImageSlimResponse


class ImagePage(BaseModel):
    items: List[ImageSlimResponse]
    total: int
    page_size: int
    page: int