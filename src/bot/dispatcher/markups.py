from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           ReplyKeyboardMarkup,
                           KeyboardButton)

inline_keyboard = [[InlineKeyboardButton(text="search", callback_data="search")]]
base_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
keyboard = [[KeyboardButton(text="search")]]
menu_commands = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)
