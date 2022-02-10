from pydantic import BaseModel, Field
from typing import Optional

class DatasetFilters(BaseModel):
    dataset__name: Optional[str] = Field(alias="dataset_name", description="Filter dataset by name")
