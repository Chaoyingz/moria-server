from typing import Any, Callable

from fastapi import FastAPI
from loguru import logger

from app.db.events import init_db_engine


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await init_db_engine(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Any:
    @logger.catch
    async def stop_app() -> None:
        ...

    return stop_app
