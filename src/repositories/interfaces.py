from abc import ABC, abstractmethod

from dtos.game import Game, CreateGame, UpdateGame


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
