import asyncio
import threading
import time
from asyncio import sleep
from typing import Any

import factory
from factory_boy_extra.tortoise_factory import TortoiseModelFactory

from core.models import GameModel, ClientModel, GameSubscriptionModel


class BaseTortoiseModelFactory(TortoiseModelFactory):
    @classmethod
    def _create(
        cls,
        model_class,
        *args: Any,
        **kwargs: Any,
    ):
        instance = model_class(*args, **kwargs)
        loop = asyncio.new_event_loop()
        thr = threading.Thread(target=loop.run_forever, name="Async Runner", daemon=True)
        thr.start()
        future = asyncio.run_coroutine_threadsafe(instance.save(), loop)
        while not future.done():
            time.sleep(0.0001)
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


class ClientModelFactory(BaseTortoiseModelFactory):
    user = factory.Sequence(lambda n: f"user-{n}")
    chat_id = factory.Sequence(lambda n: 100000000 + n)

    class Meta:
        model = ClientModel


class GameSubscriptionModelFactory(BaseTortoiseModelFactory):
    client = factory.SubFactory(ClientModelFactory)
    game = factory.SubFactory(GameModelFactory)

    class Meta:
        model = GameSubscriptionModel
