async def notify_clients_games(game_id: int):
    from services.notifier import NotifierServiceFactory

    notifier = NotifierServiceFactory.get_service()
    await notifier.notify_clients(game_id)
