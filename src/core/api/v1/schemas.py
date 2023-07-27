from typing import Optional

from pydantic.v1 import BaseModel


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


class SubscribeRequest(BaseSubscriptionRequest):
    ...


class UnsubscribeRequest(BaseSubscriptionRequest):
    ...
