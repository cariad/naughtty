# NaughTTY

[![CircleCI](https://circleci.com/gh/cariad/naughtty/tree/main.svg?style=shield)](https://circleci.com/gh/cariad/naughtty/tree/main) [![codecov](https://codecov.io/gh/cariad/naughtty/branch/main/graph/badge.svg?token=6eW7lIpCoU)](https://codecov.io/gh/cariad/naughtty) [![Documentation Status](https://readthedocs.org/projects/naughtty/badge/?version=latest)](https://naughtty.readthedocs.io/en/latest/?badge=latest)

**NaughTTY** is a CLI tool and Python package for running commands in a pseudo-terminal.

Full documentation is published at [naughtty.readthedocs.io](https://naughtty.readthedocs.io).

## Installation

**NaughTTY** requires **Python 3.8 or later** and a **compatible operating system**.

```bash
pip install naughtty
```

**NaughTTY** requires the host operating system to support forking and pseudo-terminals. GNU/Linux is good. At the time of writing, Windows is not. No guarantees are made for any operating system.

## Basic CLI usage

```bash
naughtty APP > output-with-escape-codes.txt
naughtty APP | APP-THAT-USES-ESCAPE-CODES
```

For example:

```bash
naughtty pipenv --help > help.txt
naughtty pipenv --help | less
```

Full documentation is published at [naughtty.readthedocs.io](https://naughtty.readthedocs.io).

## Basic Python usage

```python
from naughtty import NaughTTY

ntty = NaughTTY(["pipenv", "--help"])
ntty.execute()
print(ntty.output)
```

```text
Usage: \033[39m\033[1mpipenv\033[39m\033[22m [OPTIONS] COMMAND [ARGS]...

\033[39m\033[1mOptions:\033[39m\033[22m
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                \033[33m\033[1m  shell\033[39m\033[22m).
...
```

Full documentation is published at [naughtty.readthedocs.io](https://naughtty.readthedocs.io).

## 👋 Hello!

**Hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).

If you ever raise a bug, request a feature or ask a question then mention that you're a sponsor and I'll respond as a priority. Thank you!
