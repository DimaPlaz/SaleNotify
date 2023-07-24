from typing import Iterable

from core.models import GameModel
from dtos.game import Game, CreateGame, UpdateGame


class GameFactory:
    @staticmethod
    def dto_to_model(game: Game) -> GameModel:
        return GameModel(
            id=game.id,
            name=game.name,
            discount=game.discount,
            image_link=game.image_link,
            store_link=game.store_link
        )

    @staticmethod
    def model_to_dto(game: GameModel) -> Game:
        return Game(
            id=game.id,
            name=game.name,
            discount=game.discount,
            image_link=game.image_link,
            store_link=game.store_link
        )

    @staticmethod
    def create_dto_to_model(create_game: CreateGame) -> GameModel:
        return GameModel(
            name=create_game.name,
            discount=create_game.discount,
            image_link=create_game.image_link,
            store_link=create_game.store_link
        )

    @staticmethod
    def models_to_dtos(games: Iterable[GameModel]) -> list[Game]:
        return [GameFactory.model_to_dto(g) for g in games]

    @staticmethod
    def dtos_to_models(games: list[Game | UpdateGame]) -> list[GameModel]:
        return [GameFactory.dto_to_model(g) for g in games]

    @staticmethod
    def create_dtos_to_models(create_games: list[CreateGame]) -> list[GameModel]:
        return [GameFactory.create_dto_to_model(cg) for cg in create_games]
