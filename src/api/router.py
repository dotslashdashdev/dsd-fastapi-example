from fastapi import APIRouter

from api.api_v1.example import example_router
from api.api_v1.users import users_router

router = APIRouter()
router.include_router(example_router)
router.include_router(users_router)

__all__ = ["router"]
