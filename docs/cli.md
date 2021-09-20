# CLI usage

## Running a command in a pseudo-terminal

Run `naughtty` and pass in the command plus arguments to run.

For example, to capture the output of `pipenv --help`, run:

```bash
naughtty pipenv --help
```

The output might be indistinguishable from running _without_ NaughTTY, but redirects and pipes will include the original command's escape codes.

```bash
naughtty pipenv --help > help.txt
naughtty pipenv --help | less
```

## Optional configuration

!!! info
    **You probably don't need to configure anything for NaughTTY to work with your command.** These settings are only for particularly fussy applications.

To specify the pixel dimensions of characters in the pseudo-terminal, pass `--character-pixels WIDTH,HEIGHT`. For example, to specify a character size of 12 pixels wide and 24 pixels high, pass `--character-pixels 12,24`.

The specify the number of columns in the pseudo-terminal, pass `--columns COLUMNS`. For example, to request a pseudo-terminal with 120 columns, pass `--columns 120`.

!!! tip
    Passing a very large `--columns` value can help to avoid line wrapping in the output, but be aware that applications could ignore it.

To specify the number of lines in the pseudo-terminal, pass `--lines LINES`. For example, to request a pseudo-terminal with 60 lines, pass `--lines 60`.

<!-- markdownlint-disable MD046 -->
!!! danger
    The arguments above must be passed _before_ the command to run.

    `naughtty --columns 120 my-app` will run `my-app` in a pseudo-terminal with 120 columns.

    `naughtty my-app --columns 120` will run `my-app --columns 120` in a pseudo-terminal of default size.
<!-- markdownlint-enable MD046 -->
