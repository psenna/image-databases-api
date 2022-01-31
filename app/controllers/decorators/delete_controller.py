from functools import wraps
import ormar

from app.controllers.decorators.entity_not_found import entity_not_found
from app.models.user import User

def delete_controller(model: ormar.Model):
    def inner(func):
        @entity_not_found
        @wraps(func)
        async def wrapper(current_user: User, id: int):
            entity = await model.objects.get(id=id)
            return await entity.delete()
        return wrapper
    return inner