from core.tasks.utils import TortoiseConnection


async def sync_games():
    from services.synchronizer import SteamSynchronizer
    from repositories.steam_repository import SteamRepository
    from repositories.game_repository import TortoiseGameRepository
    from core.tasks import notify_clients_task

    async with TortoiseConnection():
        service = SteamSynchronizer(SteamRepository(), TortoiseGameRepository())
        async for updates in service.sync():
            for game in updates:
                notify_clients_task.apply(args=[game.id])
