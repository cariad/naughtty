from argparse import Namespace

from naughtty.cli import make_naughtty, make_response


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
            character_pixels=None,
            columns=None,
            command=["python", "tests/out-color.py"],
            lines=None,
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
