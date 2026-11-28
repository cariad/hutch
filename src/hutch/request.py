from dataclasses import dataclass

from hutch.verb import Verb


@dataclass(frozen=True)
class Request:
    """A request to take an action on a website."""

    domain: str
    """The domain of the website to act on."""

    verb: Verb
    """The action to take."""
