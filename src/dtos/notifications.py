from dataclasses import dataclass

from dtos.game import Game


@dataclass
class NotifyClient:
    client_id: int
    game: Game
