from dataclasses import dataclass
from typing import Optional

from aiogram.types import InlineKeyboardMarkup


@dataclass
class Game:
    name: str
    discount: int
    image_link: str
    store_link: str
    id: Optional[int] = None


@dataclass
class CreateGame:
    name: str
    discount: int
    image_link: str
    store_link: str


@dataclass
class UpdateGame:
    id: int
    name: str
    discount: int
    image_link: str
    store_link: str


@dataclass
class Subscription:
    client_id: int
    game_id: int


@dataclass
class CreateSubscription(Subscription):
    ...


@dataclass
class RemoveSubscription(Subscription):
    ...


@dataclass
class NotifyGameMessage:
    text: str
    image_url: str
    buttons: InlineKeyboardMarkup
