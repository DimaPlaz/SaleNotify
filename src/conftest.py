import os

import pytest

from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="function", autouse=True)
def initialize_tests(request):
    db_url = os.environ.get("TORTOISE_TEST_DB", "sqlite://:memory:")
    initializer(["core.models"], db_url=db_url, app_label="core")
    request.addfinalizer(finalizer)
