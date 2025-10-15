from pydantic import BaseModel


class ExternalJokeResponse(BaseModel):
    type: str
    setup: str
    punchline: str
    id: int
