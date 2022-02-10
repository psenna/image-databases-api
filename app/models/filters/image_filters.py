from pydantic import BaseModel, Field
from typing import Optional

class ImageFilters(BaseModel):
    dataset__name: Optional[str] = Field(alias="dataset_name", description="Filter image by dataset name")
    dataset__id: Optional[int] = Field(alias="dataset_id", description="Filter image by dataset id")
    labels__name: Optional[str] = Field(alias="label_name", description="Filter image by label name")
    labels__id: Optional[str] = Field(alias="label_id", description="Filter image by label id")