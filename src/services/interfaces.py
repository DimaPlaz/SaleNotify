from abc import ABC, abstractmethod

from dtos.client import CreateClient
from dtos.game import CreateSubscription, RemoveSubscription


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
