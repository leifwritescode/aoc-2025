from utilities import read_input, timed
from functools import reduce
from itertools import groupby


def prepare_input(example=False, strip_lines=True):
    lines = read_input(example, strip_lines)
    return lines


def part_one(input):
    split = []
    for line in input:
        split.append([x for x in line.strip().split() if x])

    result = 0
    for equation in list(zip(*split)):
        nums = [int(x) for x in equation[:-1]]
        symbol = equation[-1]
        if symbol == '+':
            result += sum(nums)
        else:
            result += reduce(lambda acc, v: acc * v, nums)

    return result

def part_two(input):
    ops = input[-1].split() # extract the ops
    lines = input[:-1] # then discard before transposing

    # transpose rows to columns
    transposed = [''.join(col) for col in zip(*lines)]
    # group by non-whitespace and then convert to int
    grouped = [list(map(int, g)) for k, g in groupby(transposed, key=lambda x: False if x.isspace() else True) if k]
    # zip grouped numbers with operations for convenience
    zipped = list(zip(grouped, ops))

    # calculate result
    result = 0
    for group, op in zipped:
        if op == '+':
            result += sum(group)
        elif op == '*':
            result += reduce(lambda acc, v: acc * v, group)

    return result


def main():
    input = prepare_input(strip_lines=False)

    res = timed(lambda: part_one(input))
    print("part 1:", res)

    res = timed(lambda: part_two(input))
    print("part 2:", res)


if __name__ == '__main__':
    main()
