from fastapi import APIRouter

from core.api.v1.endpoints.client import client_router
from core.api.v1.endpoints.games import games_router
from core.api.v1.endpoints.subscription import subscriptions_router


api_v1_router = APIRouter(prefix="/api/v1", tags=["Core"])


api_v1_router.include_router(client_router)
api_v1_router.include_router(games_router)
api_v1_router.include_router(subscriptions_router)
