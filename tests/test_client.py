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


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        (
            (),
            "https://api.bunny.net/",
        ),
        (
            ("dnszone",),
            "https://api.bunny.net/dnszone",
        ),
        (
            ("dnszone", "123"),
            "https://api.bunny.net/dnszone/123",
        ),
        (
            ("/dnszone/", "/123/"),
            "https://api.bunny.net/dnszone/123",
        ),
        (
            ("dnszone/123", "records"),
            "https://api.bunny.net/dnszone/123/records",
        ),
    ],
)
def test_make_url(
    client: Client,
    path: tuple[str, ...],
    expected: str,
) -> None:
    """Test that `make_url` joins path segments into a fully-qualified URL."""

    assert client.make_url(*path) == expected
