import emoji
from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton)

keyboard = [[KeyboardButton(text=emoji.emojize("search"))]]
menu_commands = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)
