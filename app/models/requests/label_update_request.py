from pydantic import BaseModel


class LabelUpdateRequest(BaseModel):
    name: str