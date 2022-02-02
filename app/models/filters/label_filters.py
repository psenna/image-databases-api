from pydantic import BaseModel
from typing import Optional

class LabelFilters(BaseModel):
    label_name: Optional[str]