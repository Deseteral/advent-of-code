#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy

def grid_size(grid):
    width = len(grid[0])
    height = len(grid)
    return (width, height)

def at_pos(pos, grid):
    width, height = grid_size(grid)

    x, y = pos
    if x < 0 or y < 0 or x >= width or y >= height:
        return None

    return grid[y][x]

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

def simulate(grid, lane_mode):
    next_grid = deepcopy(grid)
    width, height = grid_size(grid)

    for y in range(height):
        for x in range(width):
            current_seat = at_pos((x, y), grid)
            if current_seat == '.':
                continue

            ncount = 0
            if lane_mode:
                for ndx, ndy in neighbour_dir:
                    nx = x
                    ny = y
                    while True:
                        nx += ndx
                        ny += ndy

                        nc = at_pos((nx, ny), grid)
                        if nc == None or nc == 'L':
                            break
                        if nc == '#':
                            ncount += 1
                            break
            else:
                for nx, ny in neighbour_dir:
                    nc = at_pos((x + nx, y + ny), grid)
                    if nc == '#': ncount += 1

            if current_seat == 'L' and ncount == 0:
                next_grid[y][x] = '#'

            if current_seat == '#':
                if (lane_mode and ncount >= 5) or (not lane_mode and ncount >= 4):
                    next_grid[y][x] = 'L'

    return next_grid

def count_seats(grid):
    width, height = grid_size(grid)
    cc = 0
    for y in range(height):
        for x in range(width):
            if at_pos((x, y), grid) == '#': cc += 1
    return cc

def settle_seat_count(grid, lane_mode):
    prev_count = -1
    while True:
        grid = simulate(grid, lane_mode)
        ncc = count_seats(grid)
        if ncc == prev_count:
            break
        prev_count = ncc
    return prev_count

with open('input') as f:
    grid = [list(line) for line in f.read().splitlines()]

    part1_count = settle_seat_count(grid, False)
    print(f"part1_count {part1_count}")

    part2_count = settle_seat_count(grid, True)
    print(f"part2_count {part2_count}")
