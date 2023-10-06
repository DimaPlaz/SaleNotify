from aiogram import Dispatcher, Bot

from bot.client import APIClientFactory
from bot.dispatcher.handlers.search_handler import search_router
from bot.dispatcher.handlers.start_handler import start_router
from bot.dispatcher.handlers.subscription_handler import subscription_router
from bot.dispatcher.middlewares.auth import AuthMessageMiddleware
from broker.cache import AsyncRedisCache
from config import settings


async def init_handlers(dp: Dispatcher):
    storage = await AsyncRedisCache(host=settings.REDIS_HOST)
    client = await APIClientFactory.get_client()
    dp.message.middleware(AuthMessageMiddleware(client, storage))
    dp.include_router(start_router)
    dp.include_router(subscription_router)
    dp.include_router(search_router)


async def start_bot(dispatcher: Dispatcher, bot: Bot,  **kwargs):
    await init_handlers(dispatcher)

    if settings.TELEGRAM_WEBHOOK:  # TODO add WEBHOOK support
        await dispatcher.start_polling()
    else:
        await dispatcher.start_polling(bot)
