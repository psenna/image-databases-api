import inspect
from functools import wraps
from itertools import count
from fastapi import Depends
from app.models.user import User
from app.controllers.dependencies import user_dependencie


def require_regular_user(func):
    oldsig = inspect.signature(func)
    params = list(oldsig.parameters.values())
    params_without_current_user = [param for param in params if param.name != 'current_user']
    has_current_user = len(params) != len(params_without_current_user)
    newparam = inspect.Parameter('current_user',
                    inspect.Parameter.KEYWORD_ONLY,
                    default = Depends(user_dependencie.get_current_user))
    params_without_current_user.insert(len(params_without_current_user),newparam)
    sig = oldsig.replace(parameters = params_without_current_user)

    @wraps(func)
    async def inner(current_user: User, *args, **kwargs):
        if has_current_user:
            return await func(current_user=current_user, *args, **kwargs)
        return await func(*args, **kwargs)
    inner.__signature__ = sig
    return inner

