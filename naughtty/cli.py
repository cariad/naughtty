from argparse import ArgumentParser, Namespace
from typing import Dict, List, Optional, Tuple, Union

from naughtty.constants import DEFAULT_CHARACTER_PIXELS, DEFAULT_TERMINAL_SIZE
from naughtty.naughtty import NaughTTY
from naughtty.version import get_version


def make_namespace(cli_args: List[str]) -> Namespace:
    """Reads `cli_args` into a `Namespace`."""

    # We need to perform our own strict left-to-right reading of the arguments
    # because `ArgumentParser` can't tell if any "--help" or "--version" is
    # intended for us or the child command.

    wip: Dict[str, Union[bool, str, List[str]]] = {}
    name: Optional[str] = None

    for index, arg in enumerate(cli_args):
        if arg.startswith("--"):
            name = arg[2:].replace("-", "_")
            wip[name] = True
        else:
            if name:
                wip[name] = arg
                name = None
            else:
                wip["command"] = cli_args[index:]
                break

    return Namespace(**wip)


def make_naughtty(ns: Namespace) -> NaughTTY:
    """Makes a `NaughTTY` instance based on the given command line arguments."""

    character_pixels: Optional[Tuple[int, int]] = None

    if "character_pixels" in ns:
        parts = str(ns.character_pixels).split(",")
        character_pixels = (int(parts[0]), int(parts[1]))

    return NaughTTY(
        columns=int(ns.columns) if "columns" in ns else None,
        command=ns.command,
        character_pixels=character_pixels,
        lines=int(ns.lines) if "lines" in ns else None,
    )


def make_response(cli_args: List[str]) -> str:
    """Makes a response to the given command line arguments."""

    parser = ArgumentParser(
        description="Executes a shell command in a pseudo-terminal and prints its output to stdout.",
        epilog="Made with love by Cariad Eccleston: https://github.com/cariad/naughtty",
    )

    parser.add_argument("command", help="command", nargs="*")

    parser.add_argument(
        "--character-pixels",
        help=f"character size in pixels (default={DEFAULT_CHARACTER_PIXELS[0]},{DEFAULT_CHARACTER_PIXELS[1]})",
        metavar="WIDTH,HEIGHT",
    )

    parser.add_argument(
        "--columns",
        help=f"columns (default=system default or {DEFAULT_TERMINAL_SIZE[0]})",
    )

    parser.add_argument(
        "--lines",
        help=f"lines (default=system default or {DEFAULT_TERMINAL_SIZE[1]})",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="print the version",
    )

    args = make_namespace(cli_args)

    if "version" in args:
        return get_version()

    if "command" not in args or "help" in args:
        return parser.format_help()

    n = make_naughtty(args)
    n.execute()
    return n.output
