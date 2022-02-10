import ormar
from functools import wraps
from app.models.schemes.pagination_scheme import PaginationParameters

from app.models.user import User

def get_all_controller(model: ormar.Model, select_related=[], exclude_fields=[]):
    def inner(func):
        @wraps(func)
        async def wrapper(current_user: User, pagination_parameters: PaginationParameters):
            query = model.objects
            if len(select_related):
                query = query.select_related(select_related)
            if len(exclude_fields):
                query = query.exclude_fields(exclude_fields)
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