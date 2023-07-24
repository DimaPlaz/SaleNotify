from dtos.client import CreateClient
from repositories.client_repository import TortoiseClientRepository
from repositories.interfaces import BaseClientRepository
from services.interfaces import ClientServiceI


class ClientService(ClientServiceI):
    def __init__(self, client_repository: BaseClientRepository):
        self._client_repository = client_repository

    async def register(self, register_client: CreateClient):
        return await self._client_repository.get_or_create_client(register_client)


class ClientServiceFactory:
    @classmethod
    def get_service(cls):
        return ClientService(TortoiseClientRepository())
