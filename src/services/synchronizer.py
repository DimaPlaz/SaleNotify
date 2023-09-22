from logger.logger import get_logger
from repositories.interfaces import BaseSteamRepository, BaseGameRepository
from services.interfaces import Synchronizer
from services.utils import batch


logger = get_logger()


class SteamSynchronizer(Synchronizer):
    def __init__(self,
                 steam_repository: BaseSteamRepository,
                 game_repository: BaseGameRepository):
        self._game_repository = game_repository
        self._steam_repository = steam_repository

    async def sync(self):
        games = await self._steam_repository.get_games()

        for game_batch in batch(games, batch_size=300):
            for_create = []
            for_update = []
            names = list(map(lambda x: x.name, game_batch))
            created_games = await self._game_repository.get_games_by_names(names)
            created_games = {game.name: game for game in created_games}

            for game in game_batch:
                if game.name not in created_games:
                    for_create.append(game)
                elif game.discount != created_games[game.name].discount:
                    game.id = created_games[game.name].id
                    for_update.append(game)

            await self._game_repository.bulk_create_games(for_create)
            await self._game_repository.bulk_update_games(for_update)

            yield for_update
