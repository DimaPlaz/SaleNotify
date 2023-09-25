from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from broker.redis_client import redis
from config import settings


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
storage = RedisStorage(redis)
dp = Dispatcher(bot=bot, storage=storage)
