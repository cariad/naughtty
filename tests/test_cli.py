from argparse import Namespace
from typing import List

from pytest import mark

from naughtty.cli import make_namespace, make_naughtty, make_response


@mark.parametrize(
    "args, expect",
    [
        ([], Namespace()),
        (["--help"], Namespace(help=True)),
        (["pipenv", "--help"], Namespace(command=["pipenv", "--help"])),
        (["--lines", "30"], Namespace(lines="30")),
        (["--lines", "30", "foo"], Namespace(command=["foo"], lines="30")),
        (["foo", "--lines", "30"], Namespace(command=["foo", "--lines", "30"])),
    ],
)
def test_make_namespace(args: List[str], expect: Namespace) -> None:
    assert make_namespace(args) == expect


def test_make_naughtty__custom() -> None:
    naughtty = make_naughtty(
        Namespace(
            character_pixels="5,6",
            columns="3",
            command=["python", "tests/out-color.py"],
            lines="4",
        )
    )

    assert naughtty.character_pixels == (5, 6)
    assert naughtty.command == ["python", "tests/out-color.py"]
    assert naughtty.terminal_size == (3, 4)


def test_make_naughtty__defaults() -> None:
    naughtty = make_naughtty(
        Namespace(
            command=["python", "tests/out-color.py"],
        )
    )

    assert naughtty.character_pixels == (9, 18)
    assert naughtty.command == ["python", "tests/out-color.py"]
    assert naughtty.terminal_size == (80, 24)


def test_make_response__for_execution() -> None:
    response = make_response(["python", "tests/out-color.py"])

    assert (
        response
        == """\x1b[32mHello, world!\x1b[39m\r
Terminal width: \x1b[33m80\x1b[39m\r
Terminal height: \x1b[33m24\x1b[39m\r
"""
    )


def test_make_response__for_execution__with_help() -> None:
    response = make_response(["pipenv", "--help"])
    assert "naughtty" not in response


def test_make_response__for_help() -> None:
    response = make_response(["--help"])
    assert response.startswith("usage: ")
    assert response.endswith("Eccleston: https://github.com/cariad/naughtty\n")
    assert "naughtty" in response


def test_make_response__for_version() -> None:
    assert make_response(["--version"]) == "-1.-1.-1"
