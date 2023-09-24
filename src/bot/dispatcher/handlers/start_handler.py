from aiogram.types import Message
from aiogram.utils.markdown import hbold

from bot.client import APIClientFactory
from bot.dispatcher.markups import BASE_MARKUP


async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    chat_id = message.from_user.id
    username = message.from_user.username
    api_client = await APIClientFactory.get_client()
    await api_client.register_client(chat_id, username)
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!",
                         reply_markup=BASE_MARKUP)
