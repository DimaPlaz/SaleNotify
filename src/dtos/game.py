from dataclasses import dataclass
from typing import Optional

from aiogram.types import InlineKeyboardMarkup


SteamID = str


@dataclass
class Game:
    name: str
    discount: int
    image_link: str
    store_link: str
    steam_id: str
    search_field: str
    review_count: int
    id: Optional[int] = None


@dataclass
class CreateGame:
    steam_id: str
    name: str
    discount: int
    image_link: str
    store_link: str
    search_field: str
    review_count: int


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
