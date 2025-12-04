from utilities import read_input, timed


def prepare_input():
    lines = read_input()

    cells = { }
    h = len(lines)
    w = len(lines[0])
    for y in range(h):
        for x in range(w):
            cells[(x, y)] = lines[y][x]

    print(cells)
    return cells


def count_adjacent(cells, xy):
    deltas = [(-1, -1), (0, -1), (1, -1),
              (-1,  0),          (1,  0),
              (-1,  1), (0,  1), (1,  1)]

    counts = 0
    for dx, dy in deltas:
        nx, ny = xy[0] + dx, xy[1] + dy
        counts += 1 if cells.get((nx, ny), None) == '@' else 0

    return counts


def part_one(cells):
    return sum([1 for cell in cells.keys() if cells.get(cell) == '@' and count_adjacent(cells, cell) < 4])


def part_two(cells):
    count = 0

    while True:
        accessible = [cell for cell in cells.keys() if cells.get(cell) == '@' and count_adjacent(cells, cell) < 4]
        if not accessible:
            break
        count += len(accessible)
        cells = dict(filter(lambda x: x[0] not in accessible, cells.items()))

    return count


def main():
    input = prepare_input()

    res = timed(lambda: part_one(input))
    print("part 1:", res)

    res = timed(lambda: part_two(input))
    print("part 2:", res)


if __name__ == '__main__':
    main()
