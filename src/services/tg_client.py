from aiogram import Dispatcher, Bot

from dtos.notifications import NotifyClient


class TGClient:
    def __init__(self, bot: Bot, dp: Dispatcher):
        self._dp = dp
        self._bot = bot

    async def notify_client(self, notify_client: NotifyClient):
        ...
