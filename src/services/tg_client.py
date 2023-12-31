import asyncio

import emoji
from aiogram import Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.input_file import URLInputFile

from dtos.game import Game, NotifyGameMessage
from dtos.notifications import NotifyClient
from logger.logger import get_logger


logger = get_logger()


class NotifyGamesMessageFactory:
    @classmethod
    def game_to_message(cls, game: Game) -> NotifyGameMessage:
        text = emoji.emojize(f":red_exclamation_mark: "
                             f"Discount for the {game.name} game "
                             f"has been updated: {game.discount}%")
        inline_keyboard = [[
            InlineKeyboardButton(
                text=emoji.emojize(":cross_mark: unsubscribe"),
                callback_data=f"unsubscribe-{game.id}"),
            InlineKeyboardButton(
                text=emoji.emojize(":gear: steam"),
                url=game.store_link),
        ]]
        buttons = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return NotifyGameMessage(
            text,
            game.image_link,
            buttons
        )


class TGClient:
    def __init__(self, bot: Bot, dp: Dispatcher):
        self._dp = dp
        self._bot = bot

    @staticmethod
    async def __check_event_loop():
        # TODO fix problem with event loop breaking
        if asyncio.get_event_loop().is_closed():
            asyncio.set_event_loop(asyncio.new_event_loop())

    async def notify_client(self, notify_client: NotifyClient):
        game_message = NotifyGamesMessageFactory.game_to_message(notify_client.game)
        photo = URLInputFile(url=game_message.image_url)
        try:
            await self.__check_event_loop()
            await self._bot.send_photo(
                notify_client.chat_id,
                photo,
                caption=game_message.text,
                reply_markup=game_message.buttons
            )
        except Exception as err:
            await logger.error(f"Client notify error: {err}")

    async def send_message(self, chat_id: int, message: str):
        await self._bot.send_message(chat_id=chat_id, text=message)
