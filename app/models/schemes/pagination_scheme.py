from pydantic import BaseModel


class PaginationParameters(BaseModel):
    page: int = 1
    page_size: int = 20
 