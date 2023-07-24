from broker.celery import app


@app.task
def sync_games_task():
    import asyncio

    from core.tasks.sync_games import sync_games

    asyncio.run(sync_games())
