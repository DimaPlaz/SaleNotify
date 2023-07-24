from dataclasses import dataclass
from typing import Optional


@dataclass
class Client:
    id: int
    chat_id: int
    username: Optional[str] = None


@dataclass
class CreateClient:
    chat_id: int
    username: Optional[str] = None
