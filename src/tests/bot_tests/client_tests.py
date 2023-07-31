import asyncio
from unittest import mock

import pytest

from bot.client import APIClient
from tests.factories import GameModelFactory


@pytest.mark.asyncio
async def test_client_search_games(mocker, game_search_answer):
    response_mock = mock.Mock()
    response_mock.json.return_value = game_search_answer
    future = asyncio.Future()
    future.set_result(response_mock)
    client_mock = mocker.patch("httpx.AsyncClient.get", return_value=future)

    game = await GameModelFactory.create(name="test-client-search-game-name")
    api_client = APIClient(base_url="https://base_url")

    res = await api_client.search_games(game.name)

    assert res
