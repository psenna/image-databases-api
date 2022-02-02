from typing import Optional
from pydantic import BaseModel


class LabelResponse(BaseModel):
    id: Optional[int]
    name: Optional[str]