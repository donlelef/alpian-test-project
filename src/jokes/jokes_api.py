from typing import Annotated

from fastapi import APIRouter, Depends

from .joke_response import JokeResponse
from .joke_service import JokeService


router = APIRouter(prefix="/jokes", tags=["jokes"])


def get_joke_service() -> JokeService:
    return JokeService()


@router.get("/random")
async def get_random_joke(
    joke_service: Annotated[JokeService, Depends(get_joke_service)]
) -> JokeResponse:
    return await joke_service.get_random_joke()
