import aioredis

from config import settings


def __get_redis():
    return aioredis.from_url(settings.REDIS_URL, decode_responses=True)


redis = __get_redis()
