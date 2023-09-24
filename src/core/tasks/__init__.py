from broker.celery import celery_app


@celery_app.task
def sync_games_task():
    from core.tasks.sync_games import sync_games

    import asyncio
    asyncio.run(sync_games())


@celery_app.task
def notify_clients_task(game_id: int):
    import asyncio
    from core.tasks.notify import notify_clients_games
    asyncio.run(notify_clients_games(game_id))
