from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = [[InlineKeyboardButton("search", callback_data="search")]]
BASE_MARKUP = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
