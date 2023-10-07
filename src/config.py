from pathlib import Path
from typing import List, Optional

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    DEBUG: bool
    ENVIRONMENT: str
    SERVICE_NAME: str
    BACKEND_CORS_ORIGINS: List[str] = []

    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_WEBHOOK: Optional[str] = None

    ROOT_PATH: str = "/"
    ADMIN_PATH: str = "/"

    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_POOL_MIN_SIZE: int = 1
    POSTGRES_POOL_MAX_SIZE: int = 5
    POSTGRES_TEST_DB_NAME: Optional[str] = None

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_URL: str = "redis://localhost:6379"

    MODULES: list[str] = ["core"]
    CELERY_IMPORTS: list[str] = ["core.tasks.sync_games",
                                 "core.tasks.notify"]
    TIMEZONE: str = "UTC"
    STEAM_SEARCH_URL: str = "https://store.steampowered.com/search/results/"
    STEAM_SEARCH_COUNT: int = 100
    API_PORT: int = 8000
    SELF_URL: str = f"http://localhost:{API_PORT}"

    def get_postgres_uri(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}"
            f":{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}"
            f":{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"
        )

    def get_tortoise_config(self):
        modules_models = [f"{m}.models" for m in self.MODULES]
        modules_models.append("aerich.models")
        return {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": self.POSTGRES_HOST,
                        "port": self.POSTGRES_PORT,
                        "user": self.POSTGRES_USER,
                        "password": self.POSTGRES_PASSWORD,
                        "database": self.POSTGRES_NAME,
                        "minsize": self.POSTGRES_POOL_MIN_SIZE,
                        "maxsize": self.POSTGRES_POOL_MAX_SIZE,
                        "statement_cache_size": 0,
                    },
                },
            },
            "apps": {
                "core": {
                    "models": modules_models,
                    "default_connection": "default",
                }
            },
            "use_tz": False,
            "timezone": "UTC",
        }

    class Config:
        case_sensitive = True
        env_file = BASE_DIR / ".env"


settings = Settings()
TORTOISE_ORM = settings.get_tortoise_config()
