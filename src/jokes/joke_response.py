from pydantic import BaseModel


class JokeResponse(BaseModel):
    type: str
    text: str
