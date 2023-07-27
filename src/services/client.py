from dtos.client import CreateClient
from repositories.client_repository import TortoiseClientRepository
from repositories.interfaces import BaseClientRepository, BaseSubscriptionRepository
from repositories.subscription_repository import TortoiseSubscriptionRepository
from services.interfaces import ClientServiceI


class ClientService(ClientServiceI):
    def __init__(self,
                 client_repository: BaseClientRepository,
                 subscription_repository: BaseSubscriptionRepository):
        self._subscription_repository = subscription_repository
        self._client_repository = client_repository

    async def register(self, register_client: CreateClient):
        return await self._client_repository.get_or_create_client(register_client)

    async def unregister(self, client_id):
        await self._subscription_repository.delete_client_subscriptions(client_id)


class ClientServiceFactory:
    @classmethod
    def get_service(cls):
        return ClientService(TortoiseClientRepository(), TortoiseSubscriptionRepository())
