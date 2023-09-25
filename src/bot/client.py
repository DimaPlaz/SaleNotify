from abc import ABC, abstractmethod
from contextlib import asynccontextmanager

import httpx
from httpx import Response

from broker.cache import CacheStorageI, AsyncRedisCache
from config import settings
from core.api.v1.schemas import ClientID
from bot.dtos import Game
from logger.logger import get_logger

logger = get_logger()


class APIClientI(ABC):
    @abstractmethod
    async def search_games(self, pattern: str) -> list[Game]:
        raise NotImplementedError

    @abstractmethod
    async def register_client(self, chat_id: int, username: str | None) -> ClientID:
        raise NotImplementedError

    @abstractmethod
    async def unregister_client(self, chat_id: int):
        raise NotImplementedError

    @abstractmethod
    async def subscribe_to_game(self, chat_id: int, game_id: int):
        raise NotImplementedError

    @abstractmethod
    async def unsubscribe_from_game(self, chat_id: int, game_id: int):
        raise NotImplementedError


class APIClient(APIClientI):
    def __init__(self,
                 base_url: str,
                 cache_storage: CacheStorageI):
        self._cache_storage = cache_storage
        self._base_url = base_url

    @asynccontextmanager
    async def __client(self) -> httpx.AsyncClient:
        client = httpx.AsyncClient(base_url=self._base_url)
        try:
            yield await client.__aenter__()
        except Exception as err:
            await logger.error(err)
            await client.__aexit__(type(err), err, err.__traceback__)
        finally:
            await client.__aexit__(None, None, None)

    async def search_games(self, pattern: str) -> list[Game]:
        params = {"keyword": pattern}
        async with self.__client() as client:
            response: Response = await client.get("api/v1/games/search", params=params)
            response.raise_for_status()

            search_result = response.json()["games"]
            return [Game(**g) for g in search_result]

    async def register_client(self, chat_id: int, username: str | None) -> ClientID:
        body = {"client": {"chat_id": chat_id, "username": username}}
        async with self.__client() as client:
            response: Response = await client.post("api/v1/client/registration", json=body)
            response.raise_for_status()
            response_json = response.json()
            assert response_json["success"]
            assert response_json["client"]
            client_id = response_json["client"]["id"]
            await self._cache_storage.set(chat_id, client_id)
            return client_id

    async def unregister_client(self, chat_id: int):
        client_id = self._cache_storage.get(chat_id)
        body = {
            "client_id": client_id
        }
        async with self.__client() as client:
            response: Response = await client.delete("api/v1/client/registration", json=body)
            response.raise_for_status()
            response_json = response.json()
            assert response_json["success"]

    async def subscribe_to_game(self, chat_id: int, game_id: int):
        client_id = await self._cache_storage.get(chat_id)
        body = {
            "client_id": client_id,
            "game_id": game_id
        }
        async with self.__client() as client:
            response: Response = await client.post("api/v1/subscription/subscribe", json=body)
            response.raise_for_status()
            response_json = response.json()
            assert response_json["success"]

    async def unsubscribe_from_game(self, chat_id: int, game_id: int):
        client_id = await self._cache_storage.get(chat_id)
        body = {
            "client_id": client_id,
            "game_id": game_id
        }
        async with self.__client() as client:
            response: Response = await client.post("api/v1/subscription/unsubscribe", json=body)
            response.raise_for_status()
            response_json = response.json()
            assert response_json["success"]


class APIClientFactory:
    @classmethod
    async def get_client(cls):
        storage = await AsyncRedisCache()
        return APIClient(
            settings.SELF_URL,
            storage
        )
