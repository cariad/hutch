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

        self.host = "api.bunny.net"
        self.protocol = "https"

    def make_url(self, *path: str) -> str:
        """
        Make a fully-qualified URL to a bunny.net API endpoint.

        Args:
            path: Path segments, which will be joined with slashes.

        Returns:
            Fully-qualified URL to a bunny.net API endpoint.
        """

        resource = "/".join([p.strip("/") for p in path])
        return f"{self.protocol}://{self.host}/{resource}"
