from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import false

class UserCreateRequest(BaseModel):
    name: str
    email: str
    password: str = Field(title="User password", Optional=false)
