from abc import ABC, abstractmethod

from dtos.client import CreateClient
from dtos.game import Game, CreateGame, UpdateGame, CreateSubscription, RemoveSubscription, Subscription, Client


class BaseGameRepository(ABC):
    @abstractmethod
    async def get_games(self) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def get_games_by_names(self, names: list[str]) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def bulk_create_games(self, create_games: list[CreateGame]):
        raise NotImplementedError

    @abstractmethod
    async def bulk_update_games(self, update_games: list[UpdateGame]):
        raise NotImplementedError


class BaseSteamRepository(ABC):
    @abstractmethod
    async def get_games(self) -> list[Game]:
        raise NotImplementedError


class BaseSubscriptionsRepository(ABC):
    @abstractmethod
    async def subscribe(self, sub: CreateSubscription):
        raise NotImplementedError

    @abstractmethod
    async def unsubscribe(self, unsub: RemoveSubscription):
        raise NotImplementedError

    @abstractmethod
    async def get_client_subscriptions(self, client_id: int) -> list[Subscription]:
        raise NotImplementedError


class BaseClientRepository(ABC):
    @abstractmethod
    async def get_or_create_client(self, create_client: CreateClient) -> Client:
        raise NotImplementedError