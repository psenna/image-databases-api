from typing import List

from fastapi import APIRouter, Depends, HTTPException, Form, status
from app.config.security import create_access_token, verify_password
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.entity_not_found import entity_not_found
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.patch_controller import patch_controller
from app.models.requests.user_create_request import UserCreateRequest
from app.models.requests.user_update_request import UserUpdateRequest
from app.models.responses.page import Page
from app.models.responses.user_response import UserResponse
from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def add_user(
    create_request: UserCreateRequest,
    current_user: User = Depends(user_dependencie.get_current_superuser)
    ):
    """
    Create a new user. Only superusers can create new users.
    The user email must be unique.
    """
    properties = create_request.dict()
    properties['hash_password'] = create_request.hash_password
    del properties['password']
    entity = User(**properties)
    await entity.save()
    return entity

@router.get("/", response_model=Page[UserResponse])
@get_all_controller(User)
async def get_all_users(
    current_user: User = Depends(user_dependencie.get_current_superuser),
    page: int = 1, page_size: int = 20):
    """
    List all the user in the system. Only superusers can do this.
    """
    pass

@router.get("/{id}", response_model=UserResponse)
@get_one_controller(User)
async def get_user(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):    
    """
    Get one user by its id.
    """
    pass

@router.patch("/{id}", response_model=UserResponse)
@entity_not_found
async def patch_user(
    update_request: UserUpdateRequest, id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
    """
    Update a user. The name, email e password can be updated, only the user or a superuser can update his data.
    """
    if current_user.id != id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    stored_user = await User.objects.get(id=id)
    updated_properties = update_request.dict(exclude_unset=True)
    if "password" in updated_properties.keys():
        updated_properties['hash_password'] = updated_properties.hash_password
        del updated_properties['password']
    await stored_user.update(**updated_properties)
    return stored_user


@router.delete("/{id}")
@delete_controller(User)
async def delete_user(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_superuser)):
    """
    Delete a user. Only a superuser can delete a user.
    """
    pass

@router.post("/auth-token")
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