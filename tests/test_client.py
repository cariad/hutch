import pytest

from hutch.client import Client
from hutch.exceptions import NoApiKey


def test_api_key_is_read_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that the API key is read from the environment into the headers."""

    monkeypatch.setenv(
        "BUNNY_API_KEY",
        "test-api-key",
    )

    client = Client()

    assert client.headers == {
        "AccessKey": "test-api-key",
    }


def test_missing_api_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that a missing API key raises `NoApiKey`."""

    monkeypatch.delenv(
        "BUNNY_API_KEY",
        raising=False,
    )

    with pytest.raises(NoApiKey):
        Client()
