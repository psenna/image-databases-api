import ormar
from functools import wraps

from pydantic import BaseModel
from app.models.schemes.pagination_scheme import PaginationParameters
from app.models.user import User

def get_all_controller(model: ormar.Model, select_related=[], exclude_fields=[]):
    def inner(func):
        @wraps(func)
        async def wrapper(pagination_parameters: PaginationParameters = PaginationParameters(page=1, page_size=20), filters: BaseModel = BaseModel(), **kwargs):
            query = model.objects
            if select_related:
                query = query.select_related(select_related)
            if exclude_fields:
                query = query.exclude_fields(exclude_fields)
            query_filters = filters.dict(exclude_unset=True, exclude_none=True)
            if query_filters:
                query = query.filter(**query_filters)
            query = query.paginate(page=pagination_parameters.page, page_size=pagination_parameters.page_size)
            total = await query.count()
            return {
                "items": await query.all(),
                "total": total,
                "page_size": pagination_parameters.page_size,
                "page": pagination_parameters.page
            }
        return wrapper
    return inner