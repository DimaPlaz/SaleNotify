import structlog

from .processors import add_log_level, add_log_time, render_to_logmsg


def get_logging_config(settings):
    level = "DEBUG" if settings.DEBUG else "INFO"
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(),
                "foreign_pre_chain": [
                    structlog.stdlib.add_logger_name,
                    render_to_logmsg,
                    add_log_level,
                    add_log_time,
                ],
                "keep_exc_info": True if settings.DEBUG else False,
            },
        },
        "handlers": {
            "json": {
                "level": level,
                "class": "logging.StreamHandler",
                "formatter": "json",
            },
        },
        "loggers": {
            settings.SERVICE_NAME: {
                "handlers": ["json"],
                "level": level,
            },
            "tortoise": {
                "handlers": ["json"],
                "level": level,
            },
            "uvicorn": {
                "handlers": ["json"],
                "level": level,
            },
            "uvicorn.error": {
                "handlers": ["json"],
                "level": level,
            },
            "uvicorn.access": {
                "handlers": ["json"],
                "level": "INFO",
                "propagate": False,
            },
            "app": {
                "handlers": ["json"],
                "level": level,
            },
        },
    }
