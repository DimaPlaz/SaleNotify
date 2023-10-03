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

    async def get_clients_by_game(self, game_id: int) -> list[Client]:
        qs = await ClientModel.filter(subscriptions__game_id=game_id)
        return ClientFactory.models_to_dtos(qs)

    async def get_client_by_chat_id(self, chat_id: int) -> Client | None:
        client = await ClientModel.filter(chat_id=chat_id).first()
        if client:
            return ClientFactory.model_to_dto(client)

