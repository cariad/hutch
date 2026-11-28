from argparse import ArgumentParser
from collections.abc import Sequence
from importlib.metadata import version
from logging import DEBUG, INFO, basicConfig, getLogger

from hutch.handle import handle
from hutch.request import Request
from hutch.return_code import ReturnCode
from hutch.verb import Verb

logger = getLogger(__name__)


def main(args: Sequence[str] | None = None) -> int:
    """
    Run the `hutch` command and return its exit code.

    Args:
        args: Command line arguments.

    Returns:
        `0` if the command completed successfully
    """

    parsed = make_parser().parse_args(args)
    basicConfig(level=DEBUG if parsed.debug else INFO)

    request = Request(
        domain=parsed.domain,
        verb=Verb(parsed.verb),
    )

    handle(request)
    return ReturnCode.SUCCESS


def make_parser() -> ArgumentParser:
    """
    Make the argument parser for the `hutch` command.

    Returns:
        Argument parser.
    """

    parser = ArgumentParser(
        prog="hutch",
        description="Website hosting in bunny.net.",
    )

    parser.add_argument(
        "verb",
        choices=[verb.value for verb in Verb],
        help="action",
    )

    parser.add_argument(
        "domain",
        help="website domain",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="log debug messages",
    )

    parser.add_argument(
        "--version",
        action="version",
        help="print the version and exit",
        version=version("hutch"),
    )

    return parser
