import asyncio
from asyncio import sleep
from typing import Any

import factory
from factory_boy_extra.tortoise_factory import TortoiseModelFactory

from core.models import GameModel


class BaseTortoiseModelFactory(TortoiseModelFactory):
    @classmethod
    def _create(
        cls,
        model_class,
        *args: Any,
        **kwargs: Any,
    ):
        instance = model_class(*args, **kwargs)
        asyncio.create_task(instance.save())
        return instance

    @classmethod
    async def create(cls, **kwargs):
        res = super(BaseTortoiseModelFactory, cls).create(**kwargs)
        await sleep(0)
        return res


class GameModelFactory(BaseTortoiseModelFactory):
    name = factory.Sequence(lambda n: f"game-{n}")
    image_link = factory.Sequence(lambda n: f"http://image_link/{n}")
    store_link = factory.Sequence(lambda n: f"http://store_link/{n}")

    class Meta:
        model = GameModel
