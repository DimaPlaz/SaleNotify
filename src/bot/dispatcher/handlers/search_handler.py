import re

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, URLInputFile

from bot.client import APIClientFactory
from bot.dispatcher.constants import start_search_msg, nothing_was_found
from bot.dispatcher.handlers.message_factory import SearchGamesMessageFactory
from bot.dispatcher.markups import menu_commands
from bot.states import GameSearchState


search_router = Router()


@search_router.message(F.text == "Yummy")
async def top_games_by_discount_handler(message: Message):
    api_client = await APIClientFactory.get_client()
    games = await api_client.get_top_games_by_discount()
    game_messages = SearchGamesMessageFactory.games_to_messages(games)
    for game_message in game_messages:
        photo = URLInputFile(url=game_message.image_url)
        await message.answer_photo(photo=photo,
                                   caption=game_message.text,
                                   reply_markup=game_message.buttons)


@search_router.message(F.text == "search")
async def start_search_games_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(GameSearchState.input)
    await message.answer(start_search_msg, reply_markup=menu_commands)


@search_router.message(StateFilter(GameSearchState.input))
async def search_games_handler(message: Message, state: FSMContext) -> None:
    api_client = await APIClientFactory.get_client()
    pattern = re.sub("[^A-Za-z0-9]+", "", message.text).lower()
    games = await api_client.search_games(pattern)
    game_messages = SearchGamesMessageFactory.games_to_messages(games)
    for game_message in game_messages:
        photo = URLInputFile(url=game_message.image_url)
        await message.answer_photo(photo=photo,
                                   caption=game_message.text,
                                   reply_markup=game_message.buttons)
    if not game_messages:
        await message.answer(text=nothing_was_found)
