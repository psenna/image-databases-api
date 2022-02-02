import ormar
from functools import wraps

from app.controllers.decorators.entity_not_found import entity_not_found
from app.models.user import User

def get_one_controller(model: ormar.Model, select_related=[], exclude_fields=[], select_all=False):
    def inner(func):
        @entity_not_found
        @wraps(func)
        async def wrapper(current_user: User, id: int):
            query = model.objects
            if len(select_related):
                query = query.select_related(select_related)
            if len(exclude_fields):
                query = query.exclude_fields(exclude_fields)
            if select_all:
                query = query.select_all()
            entity = await query.get(id=id)
            return entity
        return wrapper
    return inner