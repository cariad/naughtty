from naughtty import NaughTTY


def test_naughtty() -> None:
    n = NaughTTY(["python", "tests/out-color.py"])
    n.execute()
    assert (
        n.output
        == """\x1b[32mHello, world!\x1b[39m\r
Terminal width: \x1b[33m80\x1b[39m\r
Terminal height: \x1b[33m24\x1b[39m\r
"""
    )
