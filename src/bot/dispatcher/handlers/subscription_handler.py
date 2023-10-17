from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, URLInputFile

from bot.client import APIClientFactory
from bot.dispatcher.constants import (subscribed_message,
                                      unsubscribed_message,
                                      no_subscriptions,
                                      deleted_subs,
                                      canceled_deleting_subs, share_steam_profile_msg, wishlist_sync_starter_msg)
from bot.dispatcher.handlers.message_factory import (GamesSubscribedMessageFactory,
                                                     DeleteSubsMessageFactory)
from bot.dispatcher.markups import menu_commands
from bot.states import ExportWishlistState, GameSearchState

subscription_router = Router()


@subscription_router.callback_query(F.data.startswith("subscribe-"))
async def subscribe_handler(callback: CallbackQuery) -> None:
    game_id = int(callback.data.split("-")[-1])
    chat_id = callback.from_user.id
    api_client = await APIClientFactory.get_client()
    await api_client.subscribe_to_game(chat_id, game_id)
    new_inline_keyboard = GamesSubscribedMessageFactory.reverse_inline_keyboard(
        callback.message.reply_markup,
        game_id
    )
    await callback.bot.edit_message_reply_markup(
        chat_id,
        callback.message.message_id,
        reply_markup=new_inline_keyboard
    )
    await callback.answer(text=subscribed_message, show_alert=True)


@subscription_router.callback_query(F.data.startswith("unsubscribe-"))
async def unsubscribe_handler(callback: CallbackQuery) -> None:
    game_id = int(callback.data.split("-")[-1])
    chat_id = callback.from_user.id
    api_client = await APIClientFactory.get_client()
    await api_client.unsubscribe_from_game(chat_id, game_id)
    new_inline_keyboard = GamesSubscribedMessageFactory.reverse_inline_keyboard(
        callback.message.reply_markup,
        game_id
    )
    await callback.bot.edit_message_reply_markup(
        chat_id,
        callback.message.message_id,
        reply_markup=new_inline_keyboard
    )
    await callback.answer(text=unsubscribed_message, show_alert=True)


@subscription_router.message(F.text == "my subscriptions")
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


@subscription_router.message(F.text == "delete all my subscriptions")
async def delete_my_subscriptions_handler(message: Message) -> None:
    msg = DeleteSubsMessageFactory.get_message(message.message_id)
    await message.answer(text=msg.text, reply_markup=msg.buttons)


@subscription_router.message(F.text == "export from steam wishlist")
async def export_steam_wishlist_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(ExportWishlistState.init)
    await message.answer(text=share_steam_profile_msg, reply_markup=menu_commands)


@subscription_router.message(F.text.startswith("https://"),
                             StateFilter(ExportWishlistState.init))
async def export_steam_wishlist_handler(message: Message, state: FSMContext) -> None:
    chat_id = message.from_user.id
    api_client = await APIClientFactory.get_client()
    await state.set_state(GameSearchState.input)
    await api_client.subscribe_to_games_from_wishlist(chat_id, message.text)
    await message.answer(text=wishlist_sync_starter_msg, reply_markup=menu_commands)


@subscription_router.callback_query(F.data.startswith("confirm-"))
async def confirm_delete_my_subscriptions_handler(callback: CallbackQuery) -> None:
    msg_id = int(callback.data.split("-")[-1])
    chat_id = callback.from_user.id
    api_client = await APIClientFactory.get_client()
    await api_client.delete_all_subscriptions(chat_id)
    await callback.bot.delete_message(chat_id, msg_id)
    await callback.bot.delete_message(chat_id, callback.message.message_id)
    await callback.answer(text=deleted_subs, show_alert=True)


@subscription_router.callback_query(F.data.startswith("cancel-"))
async def cancel_delete_my_subscriptions_handler(callback: CallbackQuery) -> None:
    msg_id = int(callback.data.split("-")[-1])
    chat_id = callback.from_user.id
    await callback.bot.delete_message(chat_id, msg_id)
    await callback.bot.delete_message(chat_id, callback.message.message_id)
    await callback.answer(text=canceled_deleting_subs, show_alert=True)
