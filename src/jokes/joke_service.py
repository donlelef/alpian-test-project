import httpx
from fastapi import HTTPException

from .external_joke_response import ExternalJokeResponse
from .joke_response import JokeResponse


class JokeService:
    
    def __init__(self, external_api_url: str = "https://official-joke-api.appspot.com/random_joke") -> None:
        self.external_api_url = external_api_url
    
    async def get_random_joke(self) -> JokeResponse:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.external_api_url)
                response.raise_for_status()
                
                external_joke = ExternalJokeResponse(**response.json())
                
                return JokeResponse(
                    type=external_joke.type,
                    text=f"{external_joke.setup} {external_joke.punchline}"
                )
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=502, 
                detail=f"Failed to fetch joke from external API: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500, 
                detail=f"An error occurred: {str(e)}"
            )
