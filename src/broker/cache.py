from abc import ABC, abstractmethod

from redis.asyncio import BlockingConnectionPool, Redis

from config import settings
from logger.logger import get_logger


logger = get_logger()


class CacheStorageI(ABC):
    @abstractmethod
    async def set(self, key: str | int, value: str | int):
        raise NotImplementedError

    @abstractmethod
    async def get(self, key: str | int) -> str | int | None:
        raise NotImplementedError


class AsyncRedisCache(CacheStorageI):
    def __init__(self,
                 host: str = settings.REDIS_HOST,
                 port: int = settings.REDIS_PORT,
                 max_connections: int = 10):
        self._redis_url = f"redis://{host}:{port}/5"
        self._pool = Redis.from_url(
            url=self._redis_url,
            max_connections=max_connections
        )

    def __await__(self):
        return self.init().__await__()

    async def init(self):
        await logger.info(f"redis url: {self._redis_url}")
        return self

    async def set(self, key, value):
        await self._pool.set(key, value)

    async def get(self, key):
        return await self._pool.get(key)
