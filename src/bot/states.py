from aiogram.dispatcher.filters.state import StatesGroup, State


class GameSearchState(StatesGroup):
    input = State()
    search = State()
