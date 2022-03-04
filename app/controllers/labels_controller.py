from fastapi import APIRouter, Depends
from app.controllers.decorators.create_controller import create_controller
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.patch_controller import patch_controller
from app.controllers.decorators.require_regular_user import require_regular_user
from app.models.filters.label_filters import LabelFilters
from app.models.label import Label
from app.models.schemes.label_schemes import LabelCreateRequest, LabelUpdateRequest, LabelPage, LabelResponse
from app.models.schemes.pagination_scheme import PaginationParameters
from app.models.user import User
from app.controllers.dependencies import user_dependencie

router = APIRouter()

@router.post("/", response_model=LabelResponse)
@require_regular_user
@create_controller(Label)
async def add_label(create_request: LabelCreateRequest):
    """
    Create a label.
    """

@router.get("/", response_model=LabelPage)
@require_regular_user
@get_all_controller(Label)
async def get_all_labels(
    pagination_parameters: PaginationParameters = Depends(),
    filters: LabelFilters = Depends()):
    """
    Get all labels paginated. Can filter by label name.
    """

@router.get("/{id}", response_model=LabelResponse)
@require_regular_user
@get_one_controller(Label)
async def get_one_label(
    id: int):
    """
    Get one label by id
    """    

@router.patch("/{id}", response_model=LabelResponse)
@require_regular_user
@patch_controller(Label)
async def patch_label(
    update_request: LabelUpdateRequest, id: int):
    """
    Update a label by id.
    """

@router.delete("/{id}")
@require_regular_user
@delete_controller(Label)
async def delete_label(id: int):
    """
    Remove a label
    """