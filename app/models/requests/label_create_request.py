from pydantic import BaseModel

class LabelCreateRequest(BaseModel):
    name: str