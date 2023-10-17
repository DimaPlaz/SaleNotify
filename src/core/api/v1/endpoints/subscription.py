from dataclasses import asdict

from fastapi import APIRouter, Depends
from starlette.background import BackgroundTasks

from core.api import deps
from core.api.v1 import schemas
from dtos.game import CreateSubscription, RemoveSubscription
from services.interfaces import SubscriptionServiceI

subscriptions_router = APIRouter(prefix="/subscriptions")


@subscriptions_router.get("", response_model=schemas.GamesResponse)
async def get_my_subscriptions(
        gs: schemas.GetGamesSubscribed = Depends(),
        subscription_service: SubscriptionServiceI = Depends(deps.get_subscription_service)):
    games = await subscription_service.get_games_subscribed(gs.client_id)
    return schemas.GamesResponse(success=True, games=list(map(asdict, games)))


@subscriptions_router.delete("", response_model=schemas.BaseResponse)
async def delete_my_subscriptions(
        ds: schemas.DeleteGamesSubscribed = Depends(),
        subscription_service: SubscriptionServiceI = Depends(deps.get_subscription_service)):
    await subscription_service.delete_games_subscribed(ds.client_id)
    return schemas.BaseResponse(success=True)


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


@subscriptions_router.post("/sync-wishlist", response_model=schemas.BaseResponse)
async def unsubscribe(swl: schemas.SyncWishlistRequest,
                      background_tasks: BackgroundTasks,
                      subscription_service: SubscriptionServiceI = Depends(deps.get_subscription_service)):
    if swl and subscription_service:
        background_tasks.add_task(
            subscription_service.subscribe_to_games_from_wishlist,
            client_id=swl.client_id,
            steam_profile_url=swl.steam_profile_url
        )
    return schemas.BaseResponse(success=True)
