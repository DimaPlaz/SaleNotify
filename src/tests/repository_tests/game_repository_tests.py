import pytest

from repositories.game_repository import TortoiseGameRepository
from tests.factories import GameModelFactory


@pytest.mark.asyncio
async def test_search_games_by_keyword():
    keyword = "test-keyword"
    game = await GameModelFactory.create(name=keyword)
    game_repository = TortoiseGameRepository()

    games = await game_repository.search_by_keyword(keyword)
    game_ids = [g.id for g in games]

    assert games
    assert game.id in game_ids


@pytest.mark.asyncio
async def test_bad_search_games_by_keyword():
    keyword = "bad-test-keyword"
    await GameModelFactory.create()
    game_repository = TortoiseGameRepository()

    games = await game_repository.search_by_keyword(keyword)

    assert not games
