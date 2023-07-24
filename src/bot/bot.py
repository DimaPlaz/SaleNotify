import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config import settings


def init_bot() -> tuple[Bot, Dispatcher]:
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    storage = RedisStorage2(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    loop = asyncio.get_event_loop()
    dp = Dispatcher(bot=bot, storage=storage, loop=loop)

    return bot, dp


async def _close_dispatcher(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


def start_bot(dispatcher: Dispatcher, **kwargs):
    if settings.TELEGRAM_WEBHOOK:
        executor.start_webhook(
            webhook_path=settings.TELEGRAM_WEBHOOK,
            host="0.0.0.0",
            port=8080,
            **kwargs
        )
    else:
        executor.start_polling(dispatcher)


if __name__ == '__main__':
    bot, dp = init_bot()
    start_bot(dp)
