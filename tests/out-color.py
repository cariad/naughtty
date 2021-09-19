from shutil import get_terminal_size

from ansiscape import green, sequence, yellow

print(green("Hello, world!"))

ts = get_terminal_size((-1, -1))
print(sequence("Terminal width: ", yellow(str(ts[0]))))
print(sequence("Terminal height: ", yellow(str(ts[1]))))
