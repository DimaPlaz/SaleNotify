from typing import Optional, Type, TypeVar

import aioredis

from .redis import redis

T = TypeVar("T", bound="BaseModel")


async def get_object_from_redis(key: str, cls: Type[T]) -> Optional[T]:
    try:
        data = await redis.get(key)
    except aioredis.exceptions.ConnectionError:
        return None
    if not data:
        return None
    return cls.parse_raw(data)


async def set_object_to_redis(key: str, schema: T) -> bool:
    try:
        return await redis.set(key, schema.json())
    except aioredis.exceptions.ConnectionError:
        return False
