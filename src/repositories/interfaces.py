from abc import ABC, abstractmethod

from dtos.client import CreateClient, Client
from dtos.game import Game, CreateGame, UpdateGame, CreateSubscription, RemoveSubscription, Subscription


class BaseGameRepository(ABC):
    @abstractmethod
    async def get_games(self) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def get_game_by_id(self, game_id: int) -> Game:
        raise NotImplementedError

    @abstractmethod
    async def get_games_by_names(self, names: list[str]) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def get_games_by_steam_ids(self, steam_ids: list[str]) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def bulk_create_games(self, create_games: list[CreateGame]):
        raise NotImplementedError

    @abstractmethod
    async def bulk_update_games(self, update_games: list[UpdateGame]):
        raise NotImplementedError

    @abstractmethod
    async def search_by_keyword(self, keyword: str) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def get_top_by_discount(self) -> list[Game]:
        raise NotImplementedError


class BaseSteamRepository(ABC):
    @abstractmethod
    async def get_games(self) -> list[Game]:
        raise NotImplementedError


class BaseSubscriptionRepository(ABC):
    @abstractmethod
    async def subscribe(self, sub: CreateSubscription):
        raise NotImplementedError

    @abstractmethod
    async def unsubscribe(self, unsub: RemoveSubscription):
        raise NotImplementedError

    @abstractmethod
    async def get_client_subscriptions(self, client_id: int) -> list[Subscription]:
        raise NotImplementedError

    @abstractmethod
    async def get_games_subscribed(self, client_id: int) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def delete_client_subscriptions(self, client_id: int):
        raise NotImplementedError


class BaseClientRepository(ABC):
    @abstractmethod
    async def get_or_create_client(self, create_client: CreateClient) -> Client:
        raise NotImplementedError

    @abstractmethod
    async def get_clients_by_game(self, game_id: int) -> list[Client]:
        raise NotImplementedError
