from dataclasses import dataclass

from dtos.game import Game


@dataclass
class NotifyClient:
    chat_id: int
    game: Game
