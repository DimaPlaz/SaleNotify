from abc import ABC, abstractmethod

from dtos.client import CreateClient
from dtos.game import CreateSubscription, RemoveSubscription, Game


class Synchronizer(ABC):
    @abstractmethod
    async def sync(self):
        raise NotImplementedError


class ClientServiceI(ABC):
    @abstractmethod
    async def register(self, register_client: CreateClient):
        raise NotImplementedError

    @abstractmethod
    async def unregister(self, client_id: int):
        raise NotImplementedError


class SubscriptionServiceI(ABC):
    @abstractmethod
    async def subscribe(self, create_subscription: CreateSubscription):
        raise NotImplementedError

    @abstractmethod
    async def unsubscribe(self, remove_subscription: RemoveSubscription):
        raise NotImplementedError

    @abstractmethod
    async def get_games_subscribed(self, client_id: int):
        raise NotImplementedError

    @abstractmethod
    async def delete_games_subscribed(self, client_id: int):
        raise NotImplementedError


class GamesServiceI(ABC):
    @abstractmethod
    async def search_by_keyword(self, keyword: str) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def get_top_by_discount(self) -> list[Game]:
        raise NotImplementedError


class NotifierI(ABC):
    @abstractmethod
    async def notify_clients(self, game_id: int):
        raise NotImplementedError
