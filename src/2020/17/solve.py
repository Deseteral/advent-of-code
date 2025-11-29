#!/usr/local/bin/python3
from collections import defaultdict
import itertools
from copy import deepcopy

def irange(s, e): return range(s, e+1)
def add_vectors(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])

def count_neighbours(pos):
    global grid
    neighbours_dir = list(itertools.product([0, 1, -1], repeat=4))[1:]
    return len(list(filter(
        lambda cell: cell == True,
        map(lambda nd: grid[add_vectors(pos, nd)], neighbours_dir),
    )))

def simulate(in_four_dimensions):
    global grid
    next_grid = deepcopy(grid)
    w_range = [0] if not in_four_dimensions else irange(-6, 6)

    for cell_pos in itertools.product(irange(-6, 8+6), irange(-6, 8+6), irange(-6, 6), w_range):
        ncount = count_neighbours(cell_pos)
        if grid[cell_pos]:
            next_grid[cell_pos] = (ncount == 2 or ncount == 3)
        else:
            next_grid[cell_pos] = (ncount == 3)

    grid = next_grid

def count_active():
    global grid
    return len(list(filter(lambda v: v == True, grid.values())))

def load_from_file():
    global grid
    grid = defaultdict(lambda: False)
    with open('input') as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, cell in enumerate(line):
                grid[(x, y, 0, 0)] = (cell == '#')

# part 1
load_from_file()
for _ in range(6): simulate(in_four_dimensions=False)
print(f"active cubes in three dimensions: {count_active()}")

# part 2
load_from_file()
for _ in range(6): simulate(in_four_dimensions=True)
print(f"active cubes in four dimensions: {count_active()}")
