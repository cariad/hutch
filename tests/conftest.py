import pytest

from hutch.client import Client


@pytest.fixture
def client() -> Client:
    """bunny.net API client with a test API key."""

    return Client(api_key="test-api-key")
