from typing import AsyncGenerator

import pytest
from asgi_lifespan import LifespanManager
from faker import Faker
from fastapi import FastAPI
from httpx import AsyncClient


@pytest.fixture
async def app() -> FastAPI:
    from app.main import get_application

    app = get_application()
    return app


@pytest.fixture
async def initialized_app(app: FastAPI) -> AsyncGenerator[FastAPI, None]:
    async with LifespanManager(app):
        yield app


@pytest.fixture
async def client(initialized_app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client


@pytest.fixture
async def fake() -> Faker:
    return Faker()
