from fastapi import APIRouter, Depends
from app.controllers.decorators.create_controller import create_controller
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.entity_not_found import entity_not_found
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.patch_controller import patch_controller
from app.models.label import Label
from app.models.requests.label_create_request import LabelCreateRequest
from app.models.requests.label_update_request import LabelUpdateRequest
from app.models.responses.label_response import LabelResponse
from app.models.responses.page import Page
from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=LabelResponse)
@create_controller(Label)
async def add_label(
        create_request: LabelCreateRequest,
        current_user: User = Depends(user_dependencie.get_current_user)
    ):
    """
    Create a label.
    """
    pass

@router.get("/", response_model=Page[LabelResponse])
@get_all_controller(Label)
async def get_all_labels(
    current_user: User = Depends(user_dependencie.get_current_user),
    page: int = 1, page_size: int = 20):
    """
    List all labels with pagination.
    """
    pass

@router.get("/{id}", response_model=LabelResponse)
@get_one_controller(Label)
async def get_one_label(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
    """
    Get one label by id
    """    
    pass

@router.patch("/{id}", response_model=LabelResponse)
@patch_controller(Label)
async def patch_label(
    update_request: LabelUpdateRequest, id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
    """
    Update a label by id.
    """
    pass

@router.delete("/{id}")
@entity_not_found
async def delete_label(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
    label = await Label.objects.select_all().get(id=id)
    images = label.images.copy()
    for image in images:
        await label.images.remove(image)
    return await label.delete()