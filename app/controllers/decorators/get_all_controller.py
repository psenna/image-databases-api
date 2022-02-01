import ormar
from functools import wraps

from app.models.user import User

def get_all_controller(model: ormar.Model, select_related=[], exclude_fields=[]):
    def inner(func):
        @wraps(func)
        async def wrapper(current_user: User, page: int = 1, page_size: int = 20):
            query = model.objects
            if len(select_related):
                query = query.select_related(select_related)
            if len(exclude_fields):
                query = query.exclude_fields(exclude_fields)
            return await query.paginate(page=page, page_size=page_size).all()
        return wrapper
    return inner