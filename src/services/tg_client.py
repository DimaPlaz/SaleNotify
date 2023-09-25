import emoji
from aiogram import Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.input_file import URLInputFile

from dtos.game import Game, NotifyGameMessage
from dtos.notifications import NotifyClient


class SearchGamesMessageFactory:
    @classmethod
    def game_to_message(cls, game: Game) -> NotifyGameMessage:
        text = emoji.emojize(f":exclamation: "
                             f"Discount for the {game.name} game "
                             f"has been updated: {game.discount}%")
        inline_keyboard = [[
            InlineKeyboardButton(
                text=emoji.emojize("unsubscribe:x:"),
                callback_data=f"unsubscribe-{game.id}"),
            InlineKeyboardButton(
                text=emoji.emojize("steam:gear:"),
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

    async def notify_client(self, notify_client: NotifyClient):
        game_message = SearchGamesMessageFactory.game_to_message(notify_client.game)
        photo = URLInputFile(url=game_message.image_url)
        await self._bot.send_photo(
            notify_client.chat_id,
            photo,
            caption=game_message.text,
            reply_markup=game_message.buttons
        )
