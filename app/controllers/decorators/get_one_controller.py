import ormar
from functools import wraps

from app.controllers.decorators.entity_not_found import entity_not_found

def get_one_controller(model: ormar.Model, select_related=[]):
    def inner(func):
        @entity_not_found
        @wraps(func)
        async def wrapper(id: int):
            query = model.objects
            if len(select_related):
                query = query.select_related(select_related)
            entity = await query.get(id=id)
            return entity
        return wrapper
    return inner