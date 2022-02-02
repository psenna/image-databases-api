from typing import List
from pydantic import BaseModel

from app.models.responses.user_response import UserResponse


class UserPage(BaseModel):
    items: List[UserResponse]
    total: int
    page_size: int
    page: int