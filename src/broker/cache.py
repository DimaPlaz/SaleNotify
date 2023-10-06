from abc import ABC, abstractmethod

from redis.asyncio import BlockingConnectionPool, Redis

from config import settings


class CacheStorageI(ABC):
    @abstractmethod
    async def set(self, key: str | int, value: str | int):
        raise NotImplementedError

    @abstractmethod
    async def get(self, key: str | int) -> str | int | None:
        raise NotImplementedError


class AsyncRedisCache(CacheStorageI):
    def __init__(self,
                 max_connections: int = 10,
                 host: str = settings.REDIS_HOST):
        self._host = host
        self.__pool = BlockingConnectionPool(
            decode_responses=True,
            max_connections=max_connections
        )

    def __await__(self):
        return self.init().__await__()

    async def init(self):
        self._pool = await Redis(
            host=self._host,
            connection_pool=self.__pool,
            db=5
        )  # noqa
        return self

    async def set(self, key, value):
        await self._pool.set(key, value)

    async def get(self, key):
        return await self._pool.get(key)
