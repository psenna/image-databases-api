from fastapi import APIRouter

router = APIRouter()

from app.controllers.user_controller import router as user_router
from app.controllers.dataset_controller import router as dataset_router
from app.controllers.image_controller import router as image_router
from app.controllers.labels_controller import router as labels_router


router.include_router(user_router, prefix='/users', tags=['User'])

router.include_router(dataset_router, prefix='/datasets', tags=['Dataset'])

router.include_router(image_router, prefix='/images', tags=['Image'])

router.include_router(labels_router, prefix='/labels', tags=['Label'])