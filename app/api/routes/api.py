from fastapi import APIRouter

from app.api.routes import cards

router = APIRouter()
router.include_router(cards.router, tags=["cards"], prefix="/cards")
