import structlog

from config import settings


def get_logger():
    return structlog.get_logger(settings.SERVICE_NAME)
