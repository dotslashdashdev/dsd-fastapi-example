import uvicorn
from fastapi import FastAPI

from api.router import router as api_v1_router
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(
    api_v1_router,
    prefix=settings.API_V1_STR,
)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        workers=1,
        access_log=False,
    )
