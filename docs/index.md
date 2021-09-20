# What is NaughTTY?

## The Short Answer

NaughTTY is a CLI tool and Python package for running commands in a pseudo-terminal.

## The Problem

In terminals, you can redirect command outputs to files or pipe the outputs to another command.

For example:

- `pipenv --help` prints Pipenv's help sheet to the terminal.
- `pipenv --help > help.txt` writes Pipenv's help sheet to the file `help.txt`.
- `pipenv --help | less` pipes Pipenv's help sheet to `less` for paged reading.

Some applications emit embedded escape codes to control formatting, like colours. And some of those applications will check if they're running in a non-interactive shell (i.e. being redirected or piped) then choose to omit their escape codes.

`pipenv --help`, for example, will emit colour codes when run directly in a terminal, but _won't_ include those formatting codes in redirections or pipes.

More often than not, this is a _good thing_. Formatting codes are rarely useful in redirects and pipes where they'll be read by machines rather than human operators

But sometimes -- _sometimes_ -- you want those codes.

Some applications offer some kind of argument or flag to force the codes through. `ls`, for example, will omit codes by default when directing or piping, but you can force it with `ls --color`.

Other applications, though, don't offer any way to force escape codes to be emitted. The workaround is to run the application in a _pseudo-terminal_ to fool it into believing it's interactive.

And that's where NaughTTY comes in!

## The Solution: NaughTTY

NaughTTY is a CLI tool and Python package for running commands in a pseudo-terminal and capturing their output. This allows you to fool a command into emitting escape codes during redirection and piping when it normally wouldn't.
