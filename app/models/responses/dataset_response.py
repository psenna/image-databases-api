from typing import Optional
from pydantic import BaseModel


class DatasetResponse(BaseModel):
    id: int
    name: Optional[str]