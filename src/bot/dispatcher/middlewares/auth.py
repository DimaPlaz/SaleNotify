from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from bot.client import APIClientI
from bot.dispatcher.constants import unregistered_user
from broker.cache import CacheStorageI


class AuthMessageMiddleware(BaseMiddleware):
    def __init__(self,
                 client: APIClientI,
                 storage: CacheStorageI):
        self._client = client
        self._storage = storage

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any]
    ) -> Any:
        chat_id = event.from_user.id
        client_id = await self._storage.get(chat_id)
        if not client_id:
            client = await self._client.get_client_by_chat_id(chat_id)
            if not client:
                await event.answer(text=unregistered_user)
                return
            await self._storage.set(chat_id, client.id)

        return await handler(event, data)
