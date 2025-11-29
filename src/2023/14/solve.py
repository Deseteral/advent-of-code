#!/usr/local/bin/python3
from operator import itemgetter


def get_column(cidx, level):
    return list(map(itemgetter(cidx), level))


def stringify_level(level):
    s = ''
    for y in range(len(level)):
        for x in range(len(level[0])):
            s += level[y][x]
        s += '\n'
    return s


def tilt_north(level):
    had_movement = True
    while had_movement:
        had_movement = False

        for y in range(len(level)):
            for x in range(len(level[0])):
                if level[y][x] == 'O':
                    col = get_column(x, level)[:y]
                    col = list(reversed(col))
                    h = col.index('#') if '#' in col else 999999
                    o = col.index('O') if 'O' in col else 999999
                    st = min(h, o, len(col))
                    if st > 0:
                        level[y - st][x] = 'O'
                        level[y][x] = '.'
                        had_movement = True


def rotate_level(level):
    return [list(r) for r in zip(*level[::-1])]


def calc_load(level):
    load = 0
    for y in range(len(level)):
        load += (len(level) - y) * level[y].count('O')
    return load


MAX_ITERATIONS = 1000000000


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Part 1
    level = [[c for c in line] for line in lines]
    tilt_north(level)
    print(calc_load(level))

    # Part 2
    level = [[c for c in line] for line in lines]

    # Find cycle
    cycle_hashes = [stringify_level(level)]
    cycle_hash = None
    first_cycle_iteration = None
    cycle_iteration_count = None

    for cycle in range(MAX_ITERATIONS):
        for _ in range(4):
            tilt_north(level)
            level = rotate_level(level)
        level_hash = stringify_level(level)

        if not cycle_hash:
            if level_hash in cycle_hashes:
                cycle_hash = level_hash
                first_cycle_iteration = cycle
        else:
            if level_hash == cycle_hash:
                cycle_iteration_count = cycle - first_cycle_iteration
                break

        cycle_hashes.append(level_hash)

    # Calculate iteration count of incomplete cycle
    remaining_iterations = MAX_ITERATIONS - (first_cycle_iteration + cycle_iteration_count) - 1
    rest_iterations = remaining_iterations - ((remaining_iterations // cycle_iteration_count) * cycle_iteration_count)

    for _ in range(rest_iterations):
        for _ in range(4):
            tilt_north(level)
            level = rotate_level(level)

    print(calc_load(level))


if __name__ == '__main__':
    main()
