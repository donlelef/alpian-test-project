"""End-to-end tests for the health check endpoint."""
import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(app)


def test_health_check_returns_healthy_status(client: TestClient) -> None:
    """Test that the health check endpoint returns a healthy status."""
    response = client.get("/health")
    
    assert response.status_code == 200


def test_health_check_response_contains_status_field(client: TestClient) -> None:
    """Test that the health check response contains the status field."""
    response = client.get("/health")
    
    assert "status" in response.json()


def test_health_check_status_value_is_healthy(client: TestClient) -> None:
    """Test that the health check status value is 'healthy'."""
    response = client.get("/health")
    
    assert response.json()["status"] == "healthy"


def test_health_check_response_content_type(client: TestClient) -> None:
    """Test that the health check response has the correct content type."""
    response = client.get("/health")
    
    assert response.headers["content-type"] == "application/json"
