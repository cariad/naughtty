from argparse import ArgumentParser, Namespace
from typing import List, Optional, Tuple

from naughtty.constants import DEFAULT_CHARACTER_PIXELS, DEFAULT_TERMINAL_SIZE
from naughtty.naughtty import NaughTTY
from naughtty.version import get_version


def make_naughtty(ns: Namespace) -> NaughTTY:
    """Makes a `NaughTTY` instance based on the given command line arguments."""

    character_pixels: Optional[Tuple[int, int]] = None

    if ns.char:
        parts = str(ns.char).split(",")
        character_pixels = (int(parts[0]), int(parts[1]))

    return NaughTTY(
        columns=int(ns.cols) if ns.cols else None,
        command=ns.command,
        rows=int(ns.rows) if ns.rows else None,
        character_pixels=character_pixels,
    )


def make_response(cli_args: Optional[List[str]] = None) -> str:
    """Makes a response to the given command line arguments."""

    parser = ArgumentParser(
        # We don't want ArgumentParser to pick up on "--help" in the child
        # command's arguments:
        add_help=False,
        description="Executes a shell command in a pseudo-terminal and prints its output to stdout.",
        epilog="For example: naughtty pipenv --help > out.txt",
    )

    parser.add_argument("command", help="command", nargs="*")

    parser.add_argument(
        "--char",
        help=f"character size in pixels (default={DEFAULT_CHARACTER_PIXELS[0]},{DEFAULT_CHARACTER_PIXELS[1]})",
        metavar="WIDTH,HEIGHT",
    )

    parser.add_argument(
        "--cols",
        help=f"columns (default=system default or {DEFAULT_TERMINAL_SIZE[0]})",
    )

    parser.add_argument("--help", action="store_true", help="print this help")

    parser.add_argument(
        "--rows",
        help=f"rows (default=system default or {DEFAULT_TERMINAL_SIZE[1]})",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="print the version",
    )

    args = parser.parse_args(cli_args)

    if args.version:
        return get_version()

    # If we discover "--help" AND a command then that "--help" is intended for
    # the command and not us:
    if not args.command or (args.help and not args.command):
        return parser.format_help()

    n = make_naughtty(args)
    n.execute()
    return n.output
