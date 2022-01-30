import ormar
from functools import wraps

def get_all_controller(model: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper(page: int = 1, page_size: int = 20):
                return await model.objects.paginate(page=page, page_size=page_size).all()
        return wrapper
    return inner