from typing import List

from fastapi import APIRouter, Depends, HTTPException, Form, status
from app.config.security import create_access_token, verify_password
from app.controllers.decorators.create_controller import create_controller
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.entity_not_found import entity_not_found
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.require_regular_user import require_regular_user
from app.controllers.decorators.require_super_user import require_super_user
from app.models.schemes.login_schemes import TokenResponse
from app.models.schemes.pagination_scheme import PaginationParameters
from app.models.schemes.user_schemes import UserCreateRequest, UserUpdateRequest, UserPage, UserResponse
from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=UserResponse)
@require_super_user
@create_controller(User)
async def add_user(
    create_request: UserCreateRequest):
    """
    Create a new user. Only superusers can create new users.
    The user email must be unique.
    """

@router.get("/", response_model=UserPage)
@require_super_user
@get_all_controller(User)
async def get_all_users(pagination_parameters: PaginationParameters = Depends()):
    """
    List all the user in the system. Only superusers can do this.
    """

@router.get("/{id}", response_model=UserResponse)
@require_regular_user
@get_one_controller(User)
async def get_user(id: int):    
    """
    Get one user by its id.
    """

@router.patch("/{id}", response_model=UserResponse)
@require_regular_user
@entity_not_found
async def patch_user(
    update_request: UserUpdateRequest, id: int,
    current_user: User):
    """
    Update a user. The name, email e password can be updated, only the user or a superuser can update his data.
    """
    if current_user.id != id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only the user or a superuser can update a user data",
        )
    stored_user = await User.objects.get(id=id)
    updated_properties = update_request.dict(exclude_unset=True)
    await stored_user.update(**updated_properties)
    return stored_user


@router.delete("/{id}")
@require_super_user
@delete_controller(User)
async def delete_user(id: int):
    """
    Delete a user. Only a superuser can delete a user.
    """

@router.post("/auth-token", response_model=TokenResponse)
async def login(username: str = Form(...), password: str = Form(...)):
    """
    Create a user auth token. Send the username(email) and the password.
    """
    user = await User.objects.get_or_none(email=username)
    if not user or not verify_password(password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Worng user email or password!"
                           )
    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer",
    }