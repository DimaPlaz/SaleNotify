from abc import ABC, abstractmethod

from redis.asyncio import BlockingConnectionPool, Redis

from config import settings


class CacheStorageI(ABC):
    @abstractmethod
    async def set(self, key: str | int, value: str | int):
        raise NotImplementedError

    @abstractmethod
    async def get(self, key: str | int) -> str | int:
        raise NotImplementedError


class AsyncRedisCache(CacheStorageI):
    def __init__(self,
                 max_connections: int = 10):
        self.__pool = BlockingConnectionPool(
            decode_responses=True,
            max_connections=max_connections
        )

    def __await__(self):
        return self.init().__await__()

    async def init(self):
        self._pool = await Redis(connection_pool=self.__pool)  # noqa
        return self

    async def set(self, key, value):
        await self._pool.set(key, value)

    async def get(self, key):
        return await self._pool.get(key)
