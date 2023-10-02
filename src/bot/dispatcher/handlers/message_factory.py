import emoji
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.dtos import GameMessage, BaseMessage
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
            text=text,
            image_url=game.image_link,
            buttons=buttons
        )

    @classmethod
    def games_to_messages(cls, games: list[Game]) -> list[GameMessage]:
        return [cls.game_to_message(g) for g in games]


class GamesSubscribedMessageFactory:
    @classmethod
    def game_to_message(cls, game: Game) -> GameMessage:
        text = (f"Name: {game.name}\n"
                f"Discount: {game.discount}%")
        inline_keyboard = [[
            InlineKeyboardButton(
                text=emoji.emojize("unsubscribe:cross_mark:"),
                callback_data=f"unsubscribe-{game.id}"),
            InlineKeyboardButton(
                text=emoji.emojize("steam:gear:"),
                url=game.store_link),
        ]]
        buttons = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return GameMessage(
            text=text,
            image_url=game.image_link,
            buttons=buttons
        )

    @classmethod
    def games_to_messages(cls, games: list[Game]) -> list[GameMessage]:
        return [cls.game_to_message(g) for g in games]


class DeleteSubsMessageFactory:
    @classmethod
    def get_message(cls, client_id: int, message_id: int) -> BaseMessage:
        text = "Are you sure?"
        inline_keyboard = [[
            InlineKeyboardButton(
                text=emoji.emojize(":check_mark_button: confirm"),
                callback_data=f"confirm-{message_id}"
            ),
            InlineKeyboardButton(
                text=emoji.emojize(":cross_mark: cancel"),
                callback_data=f"cancel-{message_id}"
            ),
        ]]
        buttons = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

        return BaseMessage(text=text, buttons=buttons)
