from aiogram import Dispatcher, Bot
from aiogram.types.input_file import InputFile

from dtos.notifications import NotifyClient


class TGClient:
    def __init__(self, bot: Bot, dp: Dispatcher):
        self._dp = dp
        self._bot = bot

    async def notify_client(self, notify_client: NotifyClient):
        file_name = f"{notify_client.game.name}.jpg"
        file = InputFile.from_url(notify_client.game.image_link, file_name)
        text = f"Discount updated: {notify_client.game.discount}"
        message = await self._bot.send_photo(notify_client.chat_id, file, text)
