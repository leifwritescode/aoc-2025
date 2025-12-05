from itertools import groupby
from utilities import read_input, timed


def prepare_input():
    lines = read_input()
    ranges, ids = [list(g) for k, g in groupby(lines, key=bool) if k]
    ranges = [tuple(map(int, r.split('-'))) for r in ranges]
    return ranges, ids


def part_one(input):
    ranges, ids = input
    return sum([1 for i in ids if any(int(i) in range(r[0], r[1] + 1) for r in ranges)])


def part_two(input):
    ranges, _ = input
    ranges = sorted(ranges, key=lambda x: x[0])

    end = ranges[0][1]
    current = [ranges[0]]
    components = []
    for i in ranges[1:]:
        if i[0] <= end:
            current.append(i)
            end = max(end, i[1])
        else:
            components.append(current)
            current = [i]
            end = i[1]
    components.append(current)

    extents = [(min(c, key=lambda x: x[0])[0], max(c, key=lambda x: x[1])[1]) for c in components]
    return sum(r[1] - r[0] + 1 for r in extents)


def main():
    input = prepare_input()

    res = timed(lambda: part_one(input))
    print("part 1:", res)

    res = timed(lambda: part_two(input))
    print("part 2:", res)


if __name__ == '__main__':
    main()
