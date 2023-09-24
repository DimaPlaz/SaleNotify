import asyncio

from aiogram import Dispatcher, Bot
from aiogram.utils import executor

from config import settings


async def close_dispatcher(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


async def start_bot(dispatcher: Dispatcher, bot: Bot,  **kwargs):
    if settings.TELEGRAM_WEBHOOK:  # TODO add WEBHOOK support
        await dispatcher.start_polling()
        executor.start_webhook(
            webhook_path=settings.TELEGRAM_WEBHOOK,
            host="0.0.0.0",
            port=8080,
            **kwargs
        )
    else:
        await dispatcher.start_polling(bot)
