from pydantic import BaseModel
from typing import Optional

class ImageFilters(BaseModel):
    dataset_name: Optional[str]
    label_name: Optional[str]