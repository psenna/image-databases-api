import ormar
from functools import wraps
from pydantic import BaseModel

from app.controllers.decorators.entity_not_found import entity_not_found

def patch_controller(model: ormar.Model):
    def inner(func):
        @entity_not_found
        @wraps(func)
        async def wrapper(update_request: BaseModel, id: int):
                stored_entity = await model.objects.get(id=id)
                updated_properties = update_request.dict(exclude_unset=True)
                await stored_entity.update(**updated_properties)
                return stored_entity
        return wrapper
    return inner