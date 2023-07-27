from broker.celery import celery_app


@celery_app.task
def sync_games_task():
    from core.tasks.sync_games import sync_games

    import asyncio
    asyncio.run(sync_games())
