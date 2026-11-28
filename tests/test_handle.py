from hutch.handle import handle
from hutch.request import Request
from hutch.verb import Verb


def test_handle_accepts_request() -> None:
    """Test that a request can be handled."""

    request = Request(
        verb=Verb.PREVIEW,
        domain="cariad.engineering",
    )

    handle(request)
