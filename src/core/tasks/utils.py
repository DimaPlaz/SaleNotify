from tortoise import Tortoise

from config import TORTOISE_ORM
from logger.logger import get_logger

logger = get_logger()


class TortoiseConnection:
    async def __aenter__(self):
        await Tortoise.init(config=TORTOISE_ORM)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not exc_val:
            await Tortoise.close_connections()
        else:
            await logger.error(exc_val)