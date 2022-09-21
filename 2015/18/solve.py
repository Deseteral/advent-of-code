#!/usr/local/bin/python3
from copy import deepcopy

neighbour_dir = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def get_tile(x, y, level, corners_on = False):
    size = len(level[0])

    if corners_on:
        if x == 0 and y == 0:
            return True
        if x == 0 and y == (size - 1):
            return True
        if x == (size - 1) and y == 0:
            return True
        if x == (size - 1) and y == (size - 1):
            return True

    if x < 0 or y < 0 or x >= size or y >= size:
        return False

    return level[y][x]

def count_neighbours(x, y, level, corners_on = False):
    count = 0

    for (nx, ny) in neighbour_dir:
        tx = x + nx
        ty = y + ny
        if get_tile(tx, ty, level, corners_on): count += 1

    return count

def run_simulation(steps, level, corners_on):
    size = len(level[0])

    for _ in range(steps):
        next_level = [[False for _ in range(size)] for _ in range(size)]

        for y in range(0, size):
            for x in range(0, size):
                s = get_tile(x, y, level, corners_on)
                c = count_neighbours(x, y, level, corners_on)

                if s == True:
                    if c == 2 or c == 3:
                        next_level[y][x] = True
                    else:
                        next_level[y][x] = False
                else:
                    if c == 3:
                        next_level[y][x] = True
                    else:
                        next_level[y][x] = False

        level = next_level

    count = 0
    for y in range(0, size):
        for x in range(0, size):
            if get_tile(x, y, level, corners_on): count += 1

    print(count)

with open('input') as f:
    lines = f.read().splitlines()

    level = [
        [True if x == '#' else False for x in line] for line in lines
    ]

    level2 = deepcopy(level)

    run_simulation(100, level, False)
    run_simulation(100, level2, True)
