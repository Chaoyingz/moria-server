from fastapi import FastAPI
from loguru import logger
from odmantic import AIOEngine


async def init_db_engine(app: FastAPI) -> None:
    logger.info("Initializing DB engine...")
    app.state.db = AIOEngine()
    logger.info("Initialize the db engine complete.")
