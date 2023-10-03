from fastapi import APIRouter, Depends

from core.api import deps
from core.api.v1 import schemas
from dtos.client import CreateClient
from services.interfaces import ClientServiceI

client_router = APIRouter(prefix="/client")


@client_router.post("/registration", response_model=schemas.RegistrationResponse)
async def registration(rr: schemas.RegistrationRequest,
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


@client_router.delete("/registration", response_model=schemas.BaseResponse)
async def registration(rr: schemas.RemovingRequest,
                       client_service: ClientServiceI = Depends(deps.get_client_service)):
    await client_service.unregister(rr.client_id)
    return schemas.BaseResponse(success=True)


@client_router.get("/info", response_model=schemas.GetClientResponse)
async def get_client_info_by_chat_id(gc: schemas.GetClientSchema = Depends(),
                                     client_service: ClientServiceI = Depends(deps.get_client_service)):
    client = await client_service.get_info(gc.chat_id)
    if client:
        return schemas.GetClientResponse(
            success=True,
            client=schemas.ClientSchema(
                id=client.id,
                chat_id=client.chat_id,
                username=client.username
            )
        )
    else:
        return schemas.GetClientResponse(
            success=False,
            client=None
        )
