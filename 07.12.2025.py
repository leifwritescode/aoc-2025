from utilities import read_input, timed


def prepare_input(example=False, strip_lines=True):
    lines = read_input(example, strip_lines)

    w = len(lines[0])
    h = len(lines)

    start = (0, 0)
    manifolds = []
    for y in range(h):
        for x in range(w):
            if lines[y][x] == '^':
                manifolds.append((x, y))
            elif lines[y][x] == 'S':
                start = (x, y)
    # sort the manifolds first by x, then by y
    # we can then always find the first x == tachyon_beam_origin_x, y > tachyon_beam_origin_y
    manifolds = sorted(manifolds, key=lambda p: (p[0], p[1]))
    return start, manifolds


def part_one(input):
    start, manifolds = input
    beams = set([start])
    hits = set()

    while beams:
        x, y = beams.pop()
        manifold = next(((mx, my) for mx, my in manifolds if mx == x and my > y), None)
        if manifold is not None:
            mx, my = manifold
            hits.add((mx, my))
            beams.add((mx-1, my))
            beams.add((mx+1, my))

    return len(hits)


def many_worlds_interpretation(manifolds, start):
    memo = { }

    def find_timelines(ray):
        if ray in memo:
            return memo[ray]

        # for a given ray, find the next hit. if there is none, the timeline ends here
        x, y = ray
        manifold = next(((mx, my) for mx, my in manifolds if mx == x and my > y), None)
        if manifold is None:
            memo[ray] = 1
            return memo[ray]

        # otherwise, split into two new timelines and explore them
        mx, my = manifold
        left_timelines = find_timelines((mx-1, my))
        right_timelines = find_timelines((mx+1, my))
        memo[ray] = left_timelines + right_timelines
        return memo[ray]

    return find_timelines(start)


def part_two(input):
    start, manifolds = input
    return many_worlds_interpretation(manifolds, start)


def main():
    input = prepare_input()

    res = timed(lambda: part_one(input))
    print("part 1:", res)

    res = timed(lambda: part_two(input))
    print("part 2:", res)


if __name__ == '__main__':
    main()
