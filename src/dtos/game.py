from dataclasses import dataclass
from typing import Optional


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
