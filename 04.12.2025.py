from utilities import read_input, timed


def prepare_input():
    lines = read_input()

    cells = { }
    h = len(lines)
    w = len(lines[0])
    for y in range(h):
        for x in range(w):
            if lines[y][x] in ('@'):
                cells[(x, y)] = lines[y][x]

    return cells


deltas = [(-1, -1), (0, -1), (1, -1),
          (-1,  0),          (1,  0),
          (-1,  1), (0,  1), (1,  1)]


def count_adjacent(cells, xy):
    return sum([1 for dx, dy in deltas if cells.get((xy[0] + dx, xy[1] + dy), None)])


def part_one(cells):
    return sum([1 for cell in cells.keys() if cells.get(cell) and count_adjacent(cells, cell) < 4])


def part_two(cells):
    count = 0

    while True:
        accessible = [cell for cell in cells.keys() if cells.get(cell) and count_adjacent(cells, cell) < 4]
        if not accessible:
            break
        count += len(accessible)
        for cell in accessible:
            del cells[cell]

    return count


def part_two_recursive(cells):
    accessible = dict(filter(lambda cell: count_adjacent(cells, cell[0]) < 4, cells.items()))
    if not accessible:
        return 0

    return len(accessible) + part_two_recursive({k: v for k, v in cells.items() if k not in accessible})


def main():
    input = prepare_input()

    res = timed(lambda: part_one(input))
    print("part 1:", res)

    res = timed(lambda: part_two_recursive(input))
    print("part 2:", res)


if __name__ == '__main__':
    main()
