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
class BaseMessage:
    text: str
    buttons: InlineKeyboardMarkup


@dataclass
class GameMessage(BaseMessage):
    image_url: str


@dataclass
class Client:
    chat_id: int
    id: int
    username: Optional[str] = None
