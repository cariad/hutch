from os import environ

from hutch.exceptions import NoApiKey


class Client:
    """bunny.net API client."""

    def __init__(self, api_key: str | None = None) -> None:
        """Initialise the client."""

        api_key = api_key or environ.get("BUNNY_API_KEY")

        if api_key is None:
            raise NoApiKey()

        self.headers = {
            "AccessKey": api_key,
        }
