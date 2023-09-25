import emoji
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.dtos import GameMessage
from bot.dtos import Game


class SearchGamesMessageFactory:
    @classmethod
    def game_to_message(cls, game: Game) -> GameMessage:
        text = (f"Name: {game.name}\n"
                f"Discount: {game.discount}%")
        inline_keyboard = [[
            InlineKeyboardButton(
                text=emoji.emojize("subscribe:check_mark_button:"),
                callback_data=f"subscribe-{game.id}"),
            InlineKeyboardButton(
                text=emoji.emojize("steam:gear:"),
                url=game.store_link),
        ]]
        buttons = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return GameMessage(
            text,
            game.image_link,
            buttons
        )

    @classmethod
    def games_to_messages(cls, games: list[Game]) -> list[GameMessage]:
        return [cls.game_to_message(g) for g in games]
