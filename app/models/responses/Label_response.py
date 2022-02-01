from typing import Optional
from pydantic import BaseModel


class LabelResponse(BaseModel):
    id: int
    name: Optional[str]