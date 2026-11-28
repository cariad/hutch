from enum import StrEnum


class Verb(StrEnum):
    """An action to take on a website."""

    DEPLOY = "deploy"
    PREVIEW = "preview"
