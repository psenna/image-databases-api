from pydantic import BaseModel, Field
from typing import Optional

class LabelFilters(BaseModel):
    name: Optional[str] = Field(alias='label_name', description='Filter by label name')