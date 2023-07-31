from abc import ABC, abstractmethod
from contextlib import asynccontextmanager

import httpx
from httpx import Response

from dtos.game import Game


class APIClientI(ABC):
    @abstractmethod
    async def search_games(self, pattern: str) -> list[Game]:
        raise NotImplementedError


class APIClient(APIClientI):
    def __init__(self, base_url):
        self._base_url = base_url

    @asynccontextmanager
    async def __client(self) -> httpx.AsyncClient:
        client = httpx.AsyncClient(base_url=self._base_url)
        try:
            yield await client.__aenter__()
        except Exception as err:
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
