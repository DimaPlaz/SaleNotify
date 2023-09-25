from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, StateFilter

from bot.dispatcher.handlers.search_handler import start_search_games_handler, search_games_handler
from bot.dispatcher.handlers.start_handler import command_start_handler
from bot.states import GameSearchState
from config import settings


async def init_handlers(dp: Dispatcher):
    dp.message(CommandStart())(command_start_handler)
    dp.message(F.text == "search")(start_search_games_handler)
    dp.message(StateFilter(GameSearchState.input))(search_games_handler)


async def start_bot(dispatcher: Dispatcher, bot: Bot,  **kwargs):
    await init_handlers(dispatcher)

    if settings.TELEGRAM_WEBHOOK:  # TODO add WEBHOOK support
        await dispatcher.start_polling()
    else:
        await dispatcher.start_polling(bot)
