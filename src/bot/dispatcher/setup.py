from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, StateFilter

from bot.dispatcher.handlers.search_handler import start_search_games_handler, search_games_handler
from bot.dispatcher.handlers.start_handler import command_start_handler
from bot.dispatcher.handlers.subscription_handler import subscribe_handler, unsubscribe_handler, \
    confirm_delete_my_subscriptions_handler, delete_my_subscriptions_handler, cancel_delete_my_subscriptions_handler, \
    my_subscriptions_handler
from bot.states import GameSearchState, DeleteSubsState
from config import settings


async def init_handlers(dp: Dispatcher):
    dp.message(CommandStart())(command_start_handler)
    dp.message(F.text == "delete all my subscriptions")(delete_my_subscriptions_handler)
    dp.message(F.text == "my subscriptions")(my_subscriptions_handler)
    dp.message(F.text == "search")(start_search_games_handler)
    dp.message(StateFilter(GameSearchState.input))(search_games_handler)
    dp.callback_query(F.data.startswith("confirm-"))(confirm_delete_my_subscriptions_handler)
    dp.callback_query(F.data.startswith("cancel-"))(cancel_delete_my_subscriptions_handler)
    dp.callback_query(F.data.startswith("subscribe-"))(subscribe_handler)
    dp.callback_query(F.data.startswith("unsubscribe-"))(unsubscribe_handler)


async def start_bot(dispatcher: Dispatcher, bot: Bot,  **kwargs):
    await init_handlers(dispatcher)

    if settings.TELEGRAM_WEBHOOK:  # TODO add WEBHOOK support
        await dispatcher.start_polling()
    else:
        await dispatcher.start_polling(bot)
