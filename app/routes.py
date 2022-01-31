from fastapi import APIRouter

router = APIRouter()

from app.controllers.user_controller import router as user_router
from app.controllers.dataset_controller import router as dataset_router

router.include_router(user_router, prefix='/users', tags=['User'])

router.include_router(dataset_router, prefix='/datasets', tags=['Dataset'])


