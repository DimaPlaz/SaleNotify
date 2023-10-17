from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton)

from bot.dispatcher.constants import steam_wishlist_button, yammy_button, delete_subs_button, subs_button, search_button

keyboard = [[KeyboardButton(text=search_button),
             KeyboardButton(text=yammy_button)],
            [KeyboardButton(text=subs_button),
             KeyboardButton(text=delete_subs_button)],
            [KeyboardButton(text=steam_wishlist_button)]]
menu_commands = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)
