from fastapi import Request
from odmantic import AIOEngine


async def get_db_engine(request: Request) -> AIOEngine:
    return request.app.state.db
