from datetime import timedelta

from celery import Celery
from config import settings

app = Celery(__name__)

app.conf.broker_url = settings.REDIS_URL
app.conf.result_backend = settings.REDIS_URL
app.conf.imports = settings.CELERY_IMPORTS
app.conf.timezone = settings.TIMEZONE
app.conf.beat_schedule = {
    "sync_games": {
        "task": "core.tasks.sync_games_task",
        "schedule": timedelta(seconds=1),
    },
}

app.autodiscover_tasks()
