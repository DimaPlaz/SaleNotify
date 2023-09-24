import asyncio

from bot.app import init_bot
from dtos.notifications import NotifyClient
from repositories.client_repository import TortoiseClientRepository
from repositories.game_repository import TortoiseGameRepository
from repositories.interfaces import BaseClientRepository, BaseGameRepository
from services.interfaces import NotifierI
from services.tg_client import TGClient


class NotifierService(NotifierI):
    def __init__(self,
                 client_repository: BaseClientRepository,
                 game_repository: BaseGameRepository,
                 tg_client: TGClient):
        self._tg_client = tg_client
        self._game_repository = game_repository
        self._client_repository = client_repository

    async def notify_clients(self, game_id: int):
        tasks = []
        game = await self._game_repository.get_game_by_id(game_id)
        clients = await self._client_repository.get_clients_by_game(game_id)

        for client in clients:
            notify_client_dto = NotifyClient(client.chat_id, game)
            tasks.append(self._tg_client.notify_client(notify_client_dto))

        await asyncio.gather(*tasks)


class NotifierServiceFactory:
    @classmethod
    def get_service(cls):
        bot, dp = init_bot()
        return NotifierService(
            TortoiseClientRepository(),
            TortoiseGameRepository(),
            TGClient(
                bot, dp
            )
        )
