from fastapi import HTTPException
from functools import wraps
import PIL


def data_is_not_a_valid_image(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except PIL.UnidentifiedImageError:
            raise HTTPException(status_code=400, detail="The data is not a valid image!")
    return inner

