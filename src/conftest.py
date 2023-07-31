import asyncio

import pytest
import pytest_asyncio
from httpx import AsyncClient
from pytest_asyncio.plugin import SubRequest
from tortoise import Tortoise

from tortoise.contrib.test import getDBConfig
from tortoise.exceptions import DBConnectionError, OperationalError

from main import app


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


# @pytest.fixture(scope="function", autouse=True)
# def initialize_tests(request, event_loop):
#     db_url = os.environ.get("TORTOISE_TEST_DB", "sqlite://:memory:")
#     initializer(["core.models"], db_url=db_url, app_label="core", loop=event_loop)
#     request.addfinalizer(finalizer)


@pytest.fixture(scope="session", autouse=True)
def db(request: SubRequest) -> None:
    # https://github.com/tortoise/tortoise-orm/issues/1110#issuecomment-1141969706
    config = getDBConfig(app_label="core", modules=["core.models"])

    async def _init_db() -> None:
        await Tortoise.init(config)
        try:
            await Tortoise._drop_databases()
        except (DBConnectionError, OperationalError):  # pragma: nocoverage
            pass

        await Tortoise.init(config, _create_db=True)
        await Tortoise.generate_schemas(safe=False)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(_init_db())

    request.addfinalizer(lambda: loop.run_until_complete(Tortoise._drop_databases()))


@pytest_asyncio.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client_api:
        yield client_api


@pytest.fixture()
def game_search_answer():
    return {
        "success": True,
        "games": [
            {
                "id": 1,
                "name": "test_name",
                "discount": 50,
                "image_link": "http://image_link",
                "store_link": "http://store_link"
            },
            {
                "id": 2,
                "name": "test_name-2",
                "discount": 0,
                "image_link": "http://image_link-2",
                "store_link": "http://store_link-2"
            }
        ],
        "message": None
    }
