from fastapi import APIRouter, Depends
from app.controllers.decorators.create_controller import create_controller
from app.controllers.decorators.delete_controller import delete_controller
from app.controllers.decorators.get_all_controller import get_all_controller
from app.controllers.decorators.get_one_controller import get_one_controller
from app.controllers.decorators.patch_controller import patch_controller
from app.models.filters.label_filters import LabelFilters
from app.models.label import Label
from app.models.schemes.label_schemes import LabelCreateRequest, LabelUpdateRequest, LabelPage, LabelResponse
from app.models.schemes.pagination_scheme import PaginationParameters
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

@router.get("/", response_model=LabelPage)
async def get_all_labels(
    current_user: User = Depends(user_dependencie.get_current_user),
    pagination_parameters: PaginationParameters = Depends(),
    filters: LabelFilters = Depends()):
    query = Label.objects
    if filters.label_name:
        query = query.filter(name=filters.label_name)
    query = query.paginate(page=pagination_parameters.page, page_size=pagination_parameters.page_size)
    total = await query.count()
    return {
        "items": await query.all(),
        "total": total,
        "page_size": pagination_parameters.page_size,
        "page": pagination_parameters.page
        }

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
@delete_controller(Label)
async def delete_label(
    id: int,
    current_user: User = Depends(user_dependencie.get_current_user)):
    pass