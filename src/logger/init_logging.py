import logging.config

import structlog

from .logger_config import get_logging_config
from .processors import add_log_level, add_log_time, render_to_logmsg


def init_logging(settings):
    processors = [
        add_log_level,
        add_log_time,
        render_to_logmsg,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ]

    structlog.configure(
        processors=processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.AsyncBoundLogger,
        cache_logger_on_first_use=True,
    )
    logging.config.dictConfig(get_logging_config(settings))
