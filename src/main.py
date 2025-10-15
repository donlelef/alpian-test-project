from fastapi import FastAPI
import uvicorn

from src.health.health_api import router as health_router

app = FastAPI()

# Register routers
app.include_router(health_router)


def main() -> None:
    """Run the FastAPI application with uvicorn."""
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
