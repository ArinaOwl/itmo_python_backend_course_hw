from fastapi import FastAPI

from app.routers import router as main_router
from app.user.routers import router as user_router

app = FastAPI(
    title="BaseApp",
    description="BaseApp",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(main_router)
app.include_router(user_router)
