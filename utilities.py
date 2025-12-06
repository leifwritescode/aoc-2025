import __main__
from pathlib import Path
import time

def read_input(example = False, strip_lines = True):
    path = Path(__main__.__file__)
    input_file_name = path.stem + '.txt'

    if example:
        input_file_name += "." + "example"

    input_file_absolute_path = path.with_name(input_file_name)
    with open(input_file_absolute_path, 'r') as file:
        lines = [line.strip() if strip_lines else line.replace('\n', '') for line in file]

    return lines


def timed(function):
    start = time.time()
    ret = function()
    end = time.time()
    print("finished execution in", round(end - start, 3), "seconds")
    return ret
