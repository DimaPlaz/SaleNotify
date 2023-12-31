from dataclasses import asdict

from fastapi import APIRouter, Depends

from core.api import deps
from core.api.v1 import schemas
from services.interfaces import GamesServiceI

games_router = APIRouter(prefix="/games")


@games_router.get("/search", response_model=schemas.SearchGamesResponse)
async def search_games(rr: schemas.SearchGamesRequest = Depends(),
                       games_service: GamesServiceI = Depends(deps.get_games_service)):
    games = await games_service.search_by_keyword(rr.keyword.lower())
    return schemas.SearchGamesResponse(success=True, games=list(map(asdict, games)))


@games_router.get("/top", response_model=schemas.SearchGamesResponse)
async def search_games(games_service: GamesServiceI = Depends(deps.get_games_service)):
    games = await games_service.get_top_by_discount()
    return schemas.SearchGamesResponse(success=True, games=list(map(asdict, games)))
