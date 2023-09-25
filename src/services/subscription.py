from dtos.game import RemoveSubscription, CreateSubscription
from repositories.interfaces import BaseSubscriptionRepository
from repositories.subscription_repository import TortoiseSubscriptionRepository
from services.interfaces import SubscriptionServiceI


class SubscriptionService(SubscriptionServiceI):
    def __init__(self, subscription_repository: BaseSubscriptionRepository):
        self._subscription_repository = subscription_repository

    async def subscribe(self, create_subscription: CreateSubscription):
        return await self._subscription_repository.subscribe(create_subscription)

    async def unsubscribe(self, remove_subscription: RemoveSubscription):
        return self._subscription_repository.unsubscribe(remove_subscription)


class SubscriptionServiceFactory:
    @classmethod
    def get_service(cls):
        return SubscriptionService(TortoiseSubscriptionRepository())
