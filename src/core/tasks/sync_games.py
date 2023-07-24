async def sync_games():
    from services.synchronizer import SteamSynchronizer
    from repositories.steam_repository import SteamRepository
    from repositories.game_repository import TortoiseGameRepository

    service = SteamSynchronizer(SteamRepository(), TortoiseGameRepository())
    print("Пошла Жара")
    updates = await service.sync()
    print(updates)

