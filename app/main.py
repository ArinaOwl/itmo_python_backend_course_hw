from fastapi import FastAPI

from app.routers import router as main_router
from app.words.routers import router as words_router

app = FastAPI(
    title="BaseApp",
    description="BaseApp",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(main_router)
app.include_router(words_router)
