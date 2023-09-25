from fastapi import APIRouter, Depends

from core.api import deps
from core.api.v1 import schemas
from dtos.game import CreateSubscription, RemoveSubscription
from services.interfaces import SubscriptionServiceI

subscriptions_router = APIRouter(prefix="/subscription")


@subscriptions_router.post("/subscribe", response_model=schemas.BaseResponse)
async def subscribe(sr: schemas.SubscribeRequest,
                    subscription_service: SubscriptionServiceI = Depends(deps.get_subscription_service)):
    create_subscription = CreateSubscription(sr.client_id, sr.game_id)
    await subscription_service.subscribe(create_subscription)
    return schemas.BaseResponse(success=True)


@subscriptions_router.post("/unsubscribe", response_model=schemas.BaseResponse)
async def unsubscribe(usr: schemas.UnsubscribeRequest,
                      subscription_service: SubscriptionServiceI = Depends(deps.get_subscription_service)):
    remove_subscription = RemoveSubscription(usr.client_id, usr.game_id)
    await subscription_service.unsubscribe(remove_subscription)
    return schemas.BaseResponse(success=True)
