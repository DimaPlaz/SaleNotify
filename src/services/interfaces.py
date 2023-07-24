from abc import ABC, abstractmethod


class Synchronizer(ABC):
    @abstractmethod
    async def sync(self):
        raise NotImplementedError
