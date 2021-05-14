from typing import Any

from fastapi import APIRouter, Depends
from odmantic import AIOEngine

from app.api.dependencies import get_db_engine
from app.models.domain.cards import Card

router = APIRouter()


@router.post("/", response_model=Card, name="cards:create-card")
async def create_card(card: Card, db: AIOEngine = Depends(get_db_engine)) -> Any:
    return await db.save(card)
