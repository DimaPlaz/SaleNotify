from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton)

keyboard = [[KeyboardButton(text="search")],
            [KeyboardButton(text="my subscriptions"),
             KeyboardButton(text="delete all my subscriptions")],
            [KeyboardButton(text="Yummy")]]
menu_commands = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)
