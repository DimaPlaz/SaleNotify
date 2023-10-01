from dataclasses import dataclass
from typing import Optional

from aiogram.types import InlineKeyboardMarkup


@dataclass
class Game:
    steam_id: str
    name: str
    discount: int
    image_link: str
    store_link: str
    id: Optional[int] = None


@dataclass
class GameMessage:
    text: str
    image_url: str
    buttons: InlineKeyboardMarkup
