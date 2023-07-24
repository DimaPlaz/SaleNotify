from typing import Optional

from pydantic.v1 import BaseModel


class BaseClientSchema(BaseModel):
    chat_id: int
    username: Optional[str] = None


class ClientSchema(BaseClientSchema):
    id: int


class RegistrationResponse(BaseModel):
    success: bool
    client: Optional[ClientSchema] = None


class RegistrationRequest(BaseModel):
    client: BaseClientSchema
