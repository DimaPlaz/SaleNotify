from core.models import GameModel
from dtos.game import Game, CreateGame, UpdateGame
from dtos.factories import GameFactory
from repositories.interfaces import BaseGameRepository


class TortoiseGameRepository(BaseGameRepository):
    async def get_games_by_steam_ids(self, steam_ids: list[str]) -> list[Game]:
        games = await GameModel.filter(steam_id__in=steam_ids).all()
        return GameFactory.models_to_dtos(games)

    async def get_game_by_id(self, game_id: int) -> Game:
        game = await GameModel.get(id=game_id)
        return GameFactory.model_to_dto(game)

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
        fields = ["name",
                  "store_link",
                  "image_link",
                  "search_field",
                  "review_count",
                  "discount"]
        await GameModel.bulk_update(games, fields=fields, batch_size=300)

    async def search_by_keyword(self, keyword: str) -> list[Game]:
        games = await (GameModel
                       .filter(search_field__icontains=keyword)
                       .order_by("-review_count")
                       .limit(5))
        return GameFactory.models_to_dtos(games)
