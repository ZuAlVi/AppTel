from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from src.main import app


@pytest.fixture(scope='session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url='http://testserver') as ac:
        yield ac


async def test_login(ac: AsyncClient):
    response = await ac.post("/login", json={"phone": "79092991111"})
    assert response.status_code == 200
    assert "qr_link_url" in response.json()


async def test_check_login(ac: AsyncClient):
    response = await ac.get("/check/login", params={"phone": "79092991111"})
    assert response.status_code == 200
    assert "status" in response.json()


