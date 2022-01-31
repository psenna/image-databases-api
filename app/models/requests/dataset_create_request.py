from typing import Optional
from pydantic import BaseModel


class DatasetCreateRequest(BaseModel):
    name: Optional[str]