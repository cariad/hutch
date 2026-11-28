class NoApiKey(Exception):
    """Raised when a bunny.net API key is not provided."""

    def __init__(self) -> None:
        """Initialise the exception."""

        super().__init__()
