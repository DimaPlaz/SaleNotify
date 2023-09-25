from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.client import APIClientFactory
from bot.dispatcher.handlers.message_factory import SearchGamesMessageFactory
from bot.dispatcher.markups import menu_commands
from bot.states import GameSearchState


async def start_search_games_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(GameSearchState.input)
    await message.answer("t", reply_markup=menu_commands)


async def search_games_handler(message: Message, state: FSMContext) -> None:
    api_client = await APIClientFactory.get_client()
    games = await api_client.search_games(message.text)
    game_messages = SearchGamesMessageFactory.games_to_messages(games)
    for game_message in game_messages:
        await message.answer(text=game_message.text, reply_markup=game_message.buttons)
