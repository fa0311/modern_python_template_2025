import asyncio
import random

import pytest


@pytest.fixture()
def before_fixture():
    return random.randint(1, 20)


def test_sample(before_fixture):
    assert before_fixture > 0 and before_fixture < 20


@pytest.mark.asyncio
async def test_async() -> None:
    await asyncio.sleep(1)
    assert True