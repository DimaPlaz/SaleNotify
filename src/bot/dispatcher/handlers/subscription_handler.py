from aiogram.types import Message

from bot.client import APIClientFactory


async def command_start_handler(message: Message) -> None:
    api_client = await APIClientFactory.get_client()
    await api_client