from fastapi import APIRouter

from api.api_v1.example import example_router

router = APIRouter()
router.include_router(example_router)

__all__ = ["router"]
