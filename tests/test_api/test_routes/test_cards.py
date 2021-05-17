import pytest
from faker import Faker
from fastapi import FastAPI
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_user_can_create_card(
    app: FastAPI, client: AsyncClient, fake: Faker
) -> None:
    card_data = {"question_text": fake.name(), "answer_text": fake.text()}
    response = await client.post(app.url_path_for("cards:create-card"), json=card_data)
    card = response.json()
    del card["id"]
    assert card == card_data
