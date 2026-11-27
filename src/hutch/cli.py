"""The `hutch` command line interface."""

from argparse import ArgumentParser
from collections.abc import Sequence
from importlib.metadata import version


def main(args: Sequence[str] | None = None) -> int:
    """Run the `hutch` command and return its exit code."""
    parser = make_parser()
    parser.parse_args(args)
    parser.print_help()
    return 0


def make_parser() -> ArgumentParser:
    """Make the argument parser for the `hutch` command."""
    parser = ArgumentParser(
        prog="hutch",
        description="Website hosting in bunny.net.",
    )

    parser.add_argument(
        "--version",
        action="version",
        help="print the version and exit",
        version=version("hutch"),
    )

    return parser
