#!/usr/local/bin/python3
import math
from collections import Counter

def pos_add(a,b):
    return (a[0] + b[0], a[1] + b[1])

def black_tile_count(tile_map):
    return Counter(tile_map.values())[True]

with open('input') as f:
    lines = f.read().splitlines()

    tile_map = {}

    min_x = math.inf
    max_x = -math.inf
    min_y = math.inf
    max_y = -math.inf

    for line in lines:
        x = 0
        y = 0

        # e, se, sw, w, nw, and ne
        idx = 0
        while idx < len(line):
            if line[idx] == 'e': # e
                x += 2
            elif line[idx] == 's':
                idx += 1
                if line[idx] == 'e': # se
                    x += 1
                    y -= 1
                elif line[idx] == 'w': # sw
                    x -= 1
                    y -= 1
            elif line[idx] == 'w': # w
                x -= 2
            elif line[idx] == 'n':
                idx += 1
                if line[idx] == 'w': # nw
                    x -= 1
                    y += 1
                elif line[idx] == 'e': # ne
                    x += 1
                    y += 1
            idx += 1

        if not (x, y) in tile_map:
            tile_map[(x, y)] = False
        tile_map[(x, y)] = not tile_map[(x, y)]

        min_x = min(x, min_x)
        max_x =  max(x, max_x)
        min_y = min(y, min_y)
        max_y =  max(y, max_y)

    print(black_tile_count(tile_map))

    # part 2
    for y in range(min_x - 1, max_x + 2):
        for x in range(min_x - 1, max_x + 2):
            if not (x, y) in tile_map:
                tile_map[(x, y)] = False

    neighbours_dir = [
        (1, 1),
        (2, 0),
        (1, -1),
        (-1, -1),
        (-2, 0),
        (-1, 1),
    ]
    for _ in range(100):
        next_tile_map = tile_map.copy()

        for tile_pos in tile_map:
            tile = tile_map[tile_pos]

            ncount = 0
            for nd in neighbours_dir:
                npos = pos_add(tile_pos, nd)
                if npos in tile_map:
                    if tile_map[npos] == True: ncount += 1
                else:
                    next_tile_map[npos] = False

            if tile == True: # black
                if ncount == 0 or ncount > 2:
                    next_tile_map[tile_pos] = False
            else: # white
                if ncount == 2:
                    next_tile_map[tile_pos] = True

        tile_map = next_tile_map

    print(black_tile_count(tile_map))
