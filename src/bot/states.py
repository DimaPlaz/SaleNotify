from aiogram.fsm.state import StatesGroup, State


class GameSearchState(StatesGroup):
    search = State()
    input = State()


class DeleteSubsState(StatesGroup):
    confirm = State()
    delete = State()
