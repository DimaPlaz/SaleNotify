from logger.logger import get_logger
from services.client import ClientServiceFactory

logger = get_logger()


def get_client_service():
    try:
        return ClientServiceFactory.get_service()
    except Exception as err:
        logger.error(err)
