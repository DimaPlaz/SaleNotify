from abc import ABC, abstractmethod

from dtos.client import CreateClient


class Synchronizer(ABC):
    @abstractmethod
    async def sync(self):
        raise NotImplementedError


class ClientServiceI(ABC):
    @abstractmethod
    async def register(self, register_client: CreateClient):
        raise NotImplementedError
