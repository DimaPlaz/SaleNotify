import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher.filters import CommandStart

from bot.dispatcher.handlers.start_handler import command_start_handler
from config import settings


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
storage = RedisStorage2(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
dp = Dispatcher(bot=bot, storage=storage)


dp.register_message_handler(command_start_handler, CommandStart())
