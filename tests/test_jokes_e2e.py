"""End-to-end tests for the jokes endpoint."""
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from src.jokes.joke_response import JokeResponse
from src.jokes.joke_service import JokeService
from src.main import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def mock_joke_response() -> JokeResponse:
    """Create a mock JokeResponse for testing."""
    return JokeResponse(
        type="general",
        text="Why did the chicken cross the road? To get to the other side!"
    )


def test_get_random_joke_returns_success_status(client: TestClient, mock_joke_response: JokeResponse) -> None:
    """Test that the random joke endpoint returns a 200 status code."""
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_joke_response
        
        response = client.get("/jokes/random")
        
        assert response.status_code == 200


def test_get_random_joke_response_contains_type_field(client: TestClient, mock_joke_response: JokeResponse) -> None:
    """Test that the random joke response contains the type field."""
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_joke_response
        
        response = client.get("/jokes/random")
        
        assert "type" in response.json()


def test_get_random_joke_response_contains_text_field(client: TestClient, mock_joke_response: JokeResponse) -> None:
    """Test that the random joke response contains the text field."""
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_joke_response
        
        response = client.get("/jokes/random")
        
        assert "text" in response.json()


def test_get_random_joke_response_type_matches_expected(client: TestClient, mock_joke_response: JokeResponse) -> None:
    """Test that the joke type matches the expected value."""
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_joke_response
        
        response = client.get("/jokes/random")
        
        assert response.json()["type"] == "general"


def test_get_random_joke_text_is_correct(client: TestClient, mock_joke_response: JokeResponse) -> None:
    """Test that the joke text is correct."""
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_joke_response
        
        response = client.get("/jokes/random")
        
        assert response.json()["text"] == "Why did the chicken cross the road? To get to the other side!"


def test_get_random_joke_response_content_type(client: TestClient, mock_joke_response: JokeResponse) -> None:
    """Test that the random joke response has the correct content type."""
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_joke_response
        
        response = client.get("/jokes/random")
        
        assert response.headers["content-type"] == "application/json"


def test_get_random_joke_handles_external_api_http_error(client: TestClient) -> None:
    """Test that the endpoint handles HTTP errors from the external API."""
    from fastapi import HTTPException
    
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.side_effect = HTTPException(status_code=502, detail="Failed to fetch joke from external API: Connection failed")
        
        response = client.get("/jokes/random")
        
        assert response.status_code == 502


def test_get_random_joke_error_response_contains_detail(client: TestClient) -> None:
    """Test that the error response contains a detail field."""
    from fastapi import HTTPException
    
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.side_effect = HTTPException(status_code=502, detail="Failed to fetch joke from external API: Connection failed")
        
        response = client.get("/jokes/random")
        
        assert "detail" in response.json()


def test_get_random_joke_handles_external_api_timeout(client: TestClient) -> None:
    """Test that the endpoint handles timeout errors from the external API."""
    from fastapi import HTTPException
    
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.side_effect = HTTPException(status_code=502, detail="Failed to fetch joke from external API: Request timeout")
        
        response = client.get("/jokes/random")
        
        assert response.status_code == 502


def test_get_random_joke_handles_external_api_status_error(client: TestClient) -> None:
    """Test that the endpoint handles HTTP status errors from the external API."""
    from fastapi import HTTPException
    
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.side_effect = HTTPException(status_code=502, detail="Failed to fetch joke from external API: 500 Server Error")
        
        response = client.get("/jokes/random")
        
        assert response.status_code == 502


def test_get_random_joke_handles_invalid_json_response(client: TestClient) -> None:
    """Test that the endpoint handles invalid JSON from the external API."""
    from fastapi import HTTPException
    
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.side_effect = HTTPException(status_code=500, detail="An error occurred: Invalid JSON")
        
        response = client.get("/jokes/random")
        
        assert response.status_code == 500


def test_get_random_joke_handles_missing_required_fields(client: TestClient) -> None:
    """Test that the endpoint handles missing required fields in the external API response."""
    from fastapi import HTTPException
    
    with patch.object(JokeService, "get_random_joke", new_callable=AsyncMock) as mock_get:
        mock_get.side_effect = HTTPException(status_code=500, detail="An error occurred: Missing required fields")
        
        response = client.get("/jokes/random")
        
        assert response.status_code == 500
