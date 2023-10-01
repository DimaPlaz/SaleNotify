from typing import Iterable

from core.models import GameModel, GameSubscriptionModel, ClientModel
from dtos.client import Client
from dtos.game import Game, CreateGame, UpdateGame, Subscription


class GameFactory:
    @staticmethod
    def dto_to_model(game: Game) -> GameModel:
        return GameModel(
            id=game.id,
            steam_id=game.steam_id,
            name=game.name,
            search_field=game.search_field,
            review_count=game.review_count,
            discount=game.discount,
            image_link=game.image_link,
            store_link=game.store_link
        )

    @staticmethod
    def model_to_dto(game: GameModel) -> Game:
        return Game(
            id=game.id,
            steam_id=game.steam_id,
            name=game.name,
            search_field=game.search_field,
            review_count=game.review_count,
            discount=game.discount,
            image_link=game.image_link,
            store_link=game.store_link
        )

    @staticmethod
    def create_dto_to_model(create_game: CreateGame) -> GameModel:
        return GameModel(
            steam_id=create_game.steam_id,
            name=create_game.name,
            search_field=create_game.search_field,
            review_count=create_game.review_count,
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


class SubscriptionFactory:
    @staticmethod
    def model_to_dto(model: GameSubscriptionModel) -> Subscription:
        return Subscription(
            client_id=model.client_id,  # noqa
            game_id=model.game_id       # noqa
        )

    @staticmethod
    def models_to_dtos(models: Iterable[GameSubscriptionModel]) -> list[Subscription]:
        return [SubscriptionFactory.model_to_dto(m) for m in models]


class ClientFactory:
    @staticmethod
    def model_to_dto(model: ClientModel) -> Client:
        return Client(id=model.id, username=model.user, chat_id=model.chat_id)

    @staticmethod
    def models_to_dtos(models: Iterable[ClientModel]) -> list[Client]:
        return [ClientFactory.model_to_dto(m) for m in models]
