from fastapi import APIRouter
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str


router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health_check() -> HealthResponse:
    """Health check endpoint that returns the service status."""
    return HealthResponse(status="healthy")
