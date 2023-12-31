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
                text=emoji.emojize(":check_mark_button: subscribe"),
                callback_data=f"subscribe-{game.id}"),
            InlineKeyboardButton(
                text=emoji.emojize(":gear: steam"),
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
                text=emoji.emojize(":cross_mark: unsubscribe"),
                callback_data=f"unsubscribe-{game.id}"),
            InlineKeyboardButton(
                text=emoji.emojize(":gear: steam"),
                url=game.store_link),
        ]]
        buttons = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return GameMessage(
            text=text,
            image_url=game.image_link,
            buttons=buttons
        )

    @classmethod
    def reverse_inline_keyboard(cls, markup: InlineKeyboardMarkup, game_id: int) -> InlineKeyboardMarkup:
        if markup.inline_keyboard[0][0].text.endswith(" unsubscribe"):
            markup.inline_keyboard[0][0] = InlineKeyboardButton(
                text=emoji.emojize(":check_mark_button: subscribe"),
                callback_data=f"subscribe-{game_id}"
            )
        elif markup.inline_keyboard[0][0].text.endswith(" subscribe"):
            markup.inline_keyboard[0][0] = InlineKeyboardButton(
                text=emoji.emojize(":cross_mark: unsubscribe"),
                callback_data=f"unsubscribe-{game_id}"
            )
        return markup

    @classmethod
    def games_to_messages(cls, games: list[Game]) -> list[GameMessage]:
        return [cls.game_to_message(g) for g in games]


class DeleteSubsMessageFactory:
    @classmethod
    def get_message(cls, message_id: int) -> BaseMessage:
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
