from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.client import APIClientFactory
from bot.dispatcher.constants import start_message
from bot.dispatcher.markups import menu_commands


start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    chat_id = message.from_user.id
    username = message.from_user.username
    api_client = await APIClientFactory.get_client()
    await api_client.register_client(chat_id, username)
    await message.answer(start_message, reply_markup=menu_commands)
