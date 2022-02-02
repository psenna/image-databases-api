from typing import Generic, List, TypeVar

from pydantic import BaseModel

T = TypeVar("T")

class Page(Generic[T], BaseModel):
    items: List[T]
    total: int
    page_size: int
    page: int