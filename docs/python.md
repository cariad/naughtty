# Python usage

## Running a command in a pseudo-terminal

Import the `NaughTTY` class from `naughtty` and pass in the command plus arguments to run. Invoke `execute()` to execute, then read the output from `output`.

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

## Optional configuration

!!! info
    **You probably don't need to configure anything for NaughTTY to work with your command.** These settings are only for particularly fussy applications.

To specify the pixel dimensions of characters in the pseudo-terminal, initialise with `character_pixels=(WIDTH,HEIGHT)`. For example, to specify a character size of 12 pixels wide and 24 pixels high, initialise with `character_pixels=(12,24)`.

The specify the number of columns in the pseudo-terminal, initialise with `columns=COLUMNS`. For example, to request a pseudo-terminal with 120 columns, initialise with `columns=120`.

!!! tip
    Passing a very large `columns` value can help to avoid line wrapping in the output, but be aware that applications could ignore it.

To specify the number of lines in the pseudo-terminal, initialise with `lines=LINES`. For example, to request a pseudo-terminal with 60 lines, initialise with `lines=60`.
