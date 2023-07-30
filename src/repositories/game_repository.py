from core.models import GameModel
from dtos.game import Game, CreateGame, UpdateGame
from dtos.factories import GameFactory
from repositories.interfaces import BaseGameRepository


class TortoiseGameRepository(BaseGameRepository):
    async def get_games_by_names(self, names: list[str]) -> list[Game]:
        games = await GameModel.filter(name__in=names).all()
        return GameFactory.models_to_dtos(games)

    async def get_games(self) -> list[Game]:
        games = await GameModel.all()
        return GameFactory.models_to_dtos(games)

    async def bulk_create_games(self, create_games: list[CreateGame]):
        games = GameFactory.create_dtos_to_models(create_games)
        await GameModel.bulk_create(games, batch_size=300)

    async def bulk_update_games(self, update_games: list[UpdateGame]):
        games = GameFactory.dtos_to_models(update_games)
        await GameModel.bulk_update(games, ["discount"], batch_size=300)

    async def search_by_keyword(self, keyword: str) -> list[Game]:
        games = await GameModel.filter(name__icontains=keyword)
        return GameFactory.models_to_dtos(games)
