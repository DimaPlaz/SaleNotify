from dtos.game import Game
from logger.logger import get_logger
from repositories.interfaces import BaseSteamRepository, BaseGameRepository
from services.interfaces import Synchronizer


logger = get_logger()


class SteamSynchronizer(Synchronizer):
    def __init__(self,
                 steam_repository: BaseSteamRepository,
                 game_repository: BaseGameRepository):
        self._game_repository = game_repository
        self._steam_repository = steam_repository

    @staticmethod
    def __compare(game_1: Game, game_2: Game):
        return (game_1.name == game_2.name and
                game_1.store_link == game_2.store_link and
                game_1.image_link == game_2.image_link and
                game_1.search_field == game_2.search_field and
                game_1.review_count == game_2.review_count and
                game_1.discount == game_2.discount)

    async def sync(self):
        async for game_batch in self._steam_repository.get_games():  # noqa
            for_create = []
            for_update = []
            for_notify = []
            steam_ids = list(map(lambda x: x.steam_id, game_batch))
            created_games = await self._game_repository.get_games_by_steam_ids(steam_ids)
            created_games = {game.steam_id: game for game in created_games}

            for game in game_batch:
                if game.steam_id not in created_games:
                    for_create.append(game)
                elif not self.__compare(game, created_games[game.steam_id]):
                    game.id = created_games[game.steam_id].id
                    for_update.append(game)
                    if game.discount != created_games[game.steam_id].discount:
                        for_notify.append(game)

            await self._game_repository.bulk_create_games(for_create)
            await self._game_repository.bulk_update_games(for_update)

            yield for_notify
