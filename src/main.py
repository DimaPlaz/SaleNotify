from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from config import settings
from core.api.router import api_v1_router
from logger import setup_logging


app = FastAPI(
    root_path=settings.ROOT_PATH,
    title=settings.SERVICE_NAME,
    contact={"name": "Dimon", "tg": "@dimopl"},
    description="Сервис оповещейний о скидках.",
    version="0.0.1",
)


@app.on_event("startup")
def start_event_handler():
    setup_logging(app, settings)
    register_tortoise(app, config=settings.TORTOISE_CONFIG)


# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# routers
app.include_router(api_v1_router)
