from os import environ

from hutch.exceptions import NoApiKey


class Client:
    """bunny.net API client."""

    def __init__(self, api_key: str | None = None) -> None:
        """Initialise the client."""

        api_key = api_key or environ.get("BUNNY_API_KEY")

        if not api_key:
            raise NoApiKey()

        self.headers = {
            "AccessKey": api_key,
        }
