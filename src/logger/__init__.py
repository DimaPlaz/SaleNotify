from .init_logging import init_logging
from .middleware import LoggingMiddleware


def setup_logging(app, settings):
    # app.add_middleware(LoggingMiddleware)
    init_logging(settings)
