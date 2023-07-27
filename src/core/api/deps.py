from logger.logger import get_logger
from services.client import ClientServiceFactory
from services.subscription import SubscriptionServiceFactory

logger = get_logger()


def get_client_service():
    try:
        return ClientServiceFactory.get_service()
    except Exception as err:
        logger.error(err)


def get_subscription_service():
    try:
        return SubscriptionServiceFactory.get_service()
    except Exception as err:
        logger.error(err)
