from dtos.game import Game
from repositories.game_repository import TortoiseGameRepository
from repositories.interfaces import BaseGameRepository
from services.interfaces import GamesServiceI


class GamesService(GamesServiceI):
    def __init__(self, game_repository: BaseGameRepository):
        self._game_repository = game_repository

    async def search_by_keyword(self, keyword: str) -> list[Game]:
        return await self._game_repository.search_by_keyword(keyword)


class GamesServiceFactory:
    @classmethod
    def get_service(cls):
        return GamesService(TortoiseGameRepository())
