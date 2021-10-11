from sys import argv


def cli_entry() -> None:
    from naughtty.cli import make_response

    print(make_response(argv[1:]))


if __name__ == "__main__":

    cli_entry()
