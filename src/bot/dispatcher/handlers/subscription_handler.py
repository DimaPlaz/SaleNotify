import emoji
from aiogram.types import CallbackQuery

from bot.client import APIClientFactory
from bot.dispatcher.constants import subscribed_message, unsubscribed_message


async def subscribe_handler(callback: CallbackQuery) -> None:
    game_id = callback.data.split("-")[-1]
    chat_id = callback.from_user.id
    api_client = await APIClientFactory.get_client()
    await api_client.subscribe_to_game(chat_id, game_id)
    await callback.answer(text=subscribed_message, show_alert=True)


async def unsubscribe_handler(callback: CallbackQuery) -> None:
    game_id = callback.data.split("-")[-1]
    chat_id = callback.from_user.id
    api_client = await APIClientFactory.get_client()
    await api_client.unsubscribe_from_game(chat_id, game_id)
    await callback.answer(text=unsubscribed_message, show_alert=True)
