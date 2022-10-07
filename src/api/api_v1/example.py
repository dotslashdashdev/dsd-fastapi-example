from fastapi import APIRouter, status

example_router = APIRouter()


@example_router.get(
    "/ping",
    status_code=status.HTTP_200_OK,
)
async def non_auth_health_check():
    return "pong"
