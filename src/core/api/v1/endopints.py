from fastapi import APIRouter, Depends

from core.api import deps
from core.api.v1 import schemas
from dtos.client import CreateClient
from services.interfaces import ClientServiceI

client_router = APIRouter(prefix="/client")


@client_router.post("/registration", response_model=schemas.RegistrationResponse)
async def registration(rr: schemas.RegistrationRequest = Depends(),
                       client_service: ClientServiceI = Depends(deps.get_client_service)):
    create_client = CreateClient(rr.client.chat_id, rr.client.username)
    client = await client_service.register(create_client)
    return schemas.RegistrationResponse(
        success=True,
        client=schemas.ClientSchema(
            id=client.id,
            chat_id=client.chat_id,
            username=client.username
        )
    )
