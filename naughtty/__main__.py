from naughtty import get_version


def cli_entry() -> None:
    print(f"naughtty v{get_version()}")


if __name__ == "__main__":
    cli_entry()
