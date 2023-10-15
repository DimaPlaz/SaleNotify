import asyncio
from datetime import timedelta

from celery import Celery
from tortoise import Tortoise

from config import settings, TORTOISE_ORM
from logger import init_logging


async def create_celery():
    app = Celery(__name__)
    init_logging(settings)

    app.conf.broker_url = settings.REDIS_URL
    app.conf.result_backend = settings.REDIS_URL
    app.conf.imports = settings.CELERY_IMPORTS
    app.conf.timezone = settings.TIMEZONE
    app.conf.beat_schedule = {
        "sync_games": {
            "task": "core.tasks.sync_games_task",
            "schedule": timedelta(hours=2),
        },
    }
    app.autodiscover_tasks()

    await Tortoise.init(config=TORTOISE_ORM)
    return app


celery_app = asyncio.run(create_celery())
