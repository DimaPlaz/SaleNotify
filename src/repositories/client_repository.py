from core.models import ClientModel
from dtos.client import CreateClient, Client
from dtos.factories import ClientFactory
from repositories.interfaces import BaseClientRepository


class TortoiseClientRepository(BaseClientRepository):
    async def get_or_create_client(self, create_client: CreateClient) -> Client:
        model, created = await ClientModel.get_or_create(
            chat_id=create_client.chat_id,
            defaults={"user": create_client.username}
        )
        return ClientFactory.model_to_dto(model)
