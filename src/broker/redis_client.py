from redis.asyncio import Redis

from config import settings


def __get_redis():
    return Redis.from_url(settings.REDIS_URL, decode_responses=True)


redis = __get_redis()
