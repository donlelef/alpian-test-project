from fastapi import FastAPI
import uvicorn

from src.health.health_api import router as health_router
from src.jokes.jokes_api import router as jokes_router

app = FastAPI()

# Register routers
app.include_router(health_router)
app.include_router(jokes_router)


def main() -> None:
    """Run the FastAPI application with uvicorn."""
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
