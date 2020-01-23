from typing import Dict

from fastapi import APIRouter
from starlette.responses import UJSONResponse

health_check_router = APIRouter()


@health_check_router.get(
    "/health-check", response_class=UJSONResponse,
)
async def health_check() -> Dict:
    return {"status": "OK"}
