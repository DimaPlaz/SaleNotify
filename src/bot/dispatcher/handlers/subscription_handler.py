import emoji
from aiogram.types import CallbackQuery, Message, URLInputFile

from bot.client import APIClientFactory
from bot.dispatcher.constants import subscribed_message, unsubscribed_message, no_subscriptions, deleted_subs, \
    canceled_deleting_subs
from bot.dispatcher.handlers.message_factory import GamesSubscribedMessageFactory, DeleteSubsMessageFactory


async def subscribe_handler(callback: CallbackQuery) -> None:
    game_id = callback.data.split("-")[-1]
    chat_id = callback.from_user.id
    api_client = await APIClientFactory.get_client()
    await api_client.subscribe_to_game(chat_id, game_id)
    await callback.answer(text=subscribed_message, show_alert=True)
    await callback.bot.delete_message(chat_id, callback.message.message_id)


async def unsubscribe_handler(callback: CallbackQuery) -> None:
    game_id = callback.data.split("-")[-1]
    chat_id = callback.from_user.id
    api_client = await APIClientFactory.get_client()
    await api_client.unsubscribe_from_game(chat_id, game_id)
    await callback.answer(text=unsubscribed_message, show_alert=True)
    await callback.bot.delete_message(chat_id, callback.message.message_id)


async def my_subscriptions_handler(message: Message) -> None:
    chat_id = message.from_user.id
    api_client = await APIClientFactory.get_client()
    games = await api_client.get_all_subscriptions(chat_id)
    game_messages = GamesSubscribedMessageFactory.games_to_messages(games)
    for game_message in game_messages:
        photo = URLInputFile(url=game_message.image_url)
        await message.answer_photo(photo=photo,
                                   caption=game_message.text,
                                   reply_markup=game_message.buttons)
    if not game_messages:
        await message.answer(text=no_subscriptions)


async def delete_my_subscriptions_handler(message: Message) -> None:
    chat_id = message.from_user.id
    api_client = await APIClientFactory.get_client()
    client_id = await api_client._cache_storage.get(chat_id)  # noqa
    msg = DeleteSubsMessageFactory.get_message(client_id, message.message_id)
    await message.answer(text=msg.text, reply_markup=msg.buttons)


async def confirm_delete_my_subscriptions_handler(callback: CallbackQuery) -> None:
    msg_id = int(callback.data.split("-")[-1])
    chat_id = callback.from_user.id
    api_client = await APIClientFactory.get_client()
    await api_client.delete_all_subscriptions(chat_id)
    await callback.bot.delete_message(chat_id, msg_id)
    await callback.bot.delete_message(chat_id, callback.message.message_id)
    await callback.answer(text=deleted_subs, show_alert=True)


async def cancel_delete_my_subscriptions_handler(callback: CallbackQuery) -> None:
    msg_id = int(callback.data.split("-")[-1])
    chat_id = callback.from_user.id
    await callback.bot.delete_message(chat_id, msg_id)
    await callback.bot.delete_message(chat_id, callback.message.message_id)
    await callback.answer(text=canceled_deleting_subs, show_alert=True)
