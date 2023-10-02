from typing import Optional

from pydantic import BaseModel


ClientID = int


class BaseResponse(BaseModel):
    success: bool


class BaseClientSchema(BaseModel):
    chat_id: int
    username: Optional[str] = None


class ClientSchema(BaseClientSchema):
    id: int


class RegistrationResponse(BaseResponse):
    client: Optional[ClientSchema] = None


class RegistrationRequest(BaseModel):
    client: BaseClientSchema


class RemovingRequest(BaseModel):
    client_id: int


class BaseSubscriptionRequest(BaseModel):
    client_id: int
    game_id: int


class BaseSubscriptionListRequest(BaseModel):
    client_id: int


class GetGamesSubscribed(BaseSubscriptionListRequest):
    ...


class DeleteGamesSubscribed(BaseSubscriptionListRequest):
    ...


class SubscribeRequest(BaseSubscriptionRequest):
    ...


class UnsubscribeRequest(BaseSubscriptionRequest):
    ...


class BaseGameSchema(BaseModel):
    id: int
    steam_id: str
    name: str
    discount: int
    image_link: str
    store_link: str


class SearchGamesRequest(BaseModel):
    keyword: str


class SearchGamesResponse(BaseResponse):
    games: Optional[list[BaseGameSchema]] = None
    message: Optional[str] = None


class GamesResponse(BaseResponse):
    games: Optional[list[BaseGameSchema]] = None
