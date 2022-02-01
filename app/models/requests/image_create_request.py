from pydantic import BaseModel

from app.utils.image_utils import get_b64thumbnail_from_b64image


class ImageCreateRequest(BaseModel):
    name: str
    data: bytes
    dataset: int

    @property
    def thumbnail(self) -> str:
        return get_b64thumbnail_from_b64image(self.data)