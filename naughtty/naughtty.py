from fcntl import ioctl
from os import environ, execvpe, read
from pty import CHILD, fork
from shutil import get_terminal_size
from struct import pack
from termios import TIOCSWINSZ
from typing import List, Optional, Tuple

from naughtty.constants import DEFAULT_CHARACTER_PIXELS, DEFAULT_TERMINAL_SIZE


class NaughTTY:
    """
    Executes a shell command in a pseudo-terminal.

    Arguments:
        command:          Command with arguments to execute

        character_pixels: Pixel width and height of pseudo-terminal characters
                          (default=naughtty.constants.DEFAULT_CHARACTER_PIXELS)

        columns:          Pseudo-terminal column count (default=current or
                          naughtty.constants.DEFAULT_TERMINAL_SIZE[0])

        lines:            Pseudo-terminal line count (default=current or
                          naughtty.constants.DEFAULT_TERMINAL_SIZE[1])
    """

    def __init__(
        self,
        command: List[str],
        character_pixels: Optional[Tuple[int, int]] = None,
        columns: Optional[int] = None,
        lines: Optional[int] = None,
    ) -> None:

        current_terminal_size = get_terminal_size(DEFAULT_TERMINAL_SIZE)

        self._child_output = ""

        self.character_pixels = character_pixels or DEFAULT_CHARACTER_PIXELS
        self.command = command
        self.terminal_size = (
            columns or current_terminal_size.columns,
            lines or current_terminal_size.lines,
        )

    def execute(self) -> None:
        """Executes the command in a pseudo-terminal."""

        pid, fd = fork()

        # We intentionally exclude this `if` from coverage reports because the
        # case where `pid == CHILD` only ever occurs in the fork and not _this_
        # process, so the watcher doesn't know it gets touched.
        if pid != CHILD:  # pragma: no cover
            # Packed structure documentation:
            # https://www.delorie.com/djgpp/doc/libc/libc_495.html
            child_terminal_size = pack(
                "HHHH",
                self.terminal_size[1],
                self.terminal_size[0],
                self.terminal_size[0] * self.character_pixels[0],
                self.terminal_size[1] * self.character_pixels[1],
            )
            # TIOCSWINSZ = Terminal Input/Output Control Set WINdow SiZe
            ioctl(fd, TIOCSWINSZ, child_terminal_size)

        if pid == CHILD:
            # The first argument is the name, not the executable.
            #
            # `execvpe` will terminate the child when its process is complete.
            #
            # Also note that we intentionally exclude this `if` branch from
            # coverage reports because it only ever runs in the fork and not
            # _this_ process, so the watcher doesn't know it gets touched.
            execvpe(self.command[0], self.command, environ)  # pragma: no cover

        child_output = bytes()

        try:
            while True:
                child_output += read(fd, 1024)
        except OSError:
            # The child has terminated and there's nothing more to read.
            pass

        self._child_output = child_output.decode("UTF-8")

    @property
    def output(self) -> str:
        """Gets the execution's output."""

        return self._child_output
