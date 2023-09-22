import pytest

from core.models import ClientModel
from repositories.client_repository import TortoiseClientRepository
from tests.factories import ClientModelFactory, GameSubscriptionModelFactory, GameModelFactory


@pytest.mark.asyncio
async def test_get_clients_by_game():
    client_1 = await ClientModelFactory.create()
    client_2 = await ClientModelFactory.create()
    game_1 = await GameModelFactory.create()
    game_2 = await GameModelFactory.create()
    await GameSubscriptionModelFactory.create(client=client_1, game=game_1)
    await GameSubscriptionModelFactory.create(client=client_2, game=game_1)
    await GameSubscriptionModelFactory.create(client=client_2, game=game_2)

    client_repository = TortoiseClientRepository()

    clients = await client_repository.get_clients_by_game(game_1.id)

    assert len(clients) == 2
