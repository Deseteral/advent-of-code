#!/usr/local/bin/python3
from collections import defaultdict
from copy import deepcopy

ROCK = 1
GENERATOR = 2
SAND = 3

class Tile:
    def __init__(self, x, y, type):
        self.pos = (x, y)
        self.type = type

def simulate(level, max_y, detect_floor):
    active_tile = Tile(500, 0, SAND)
    rest_count = 0

    while True:
        npos = (active_tile.pos[0], active_tile.pos[1]+1)

        if detect_floor:
            if active_tile.pos[1] == (max_y + 1):
                level[active_tile.pos] = active_tile
                active_tile = Tile(500, 0, SAND)
                rest_count += 1
                continue
        else:
            if npos[1] > max_y+3: break

        if level[npos] == None:
            active_tile.pos = npos
            continue
        else:
            npos = (npos[0]-1, npos[1])
            if level[npos] == None:
                active_tile.pos = npos
                continue
            else:
                npos = (npos[0]+2, npos[1])
                if level[npos] == None:
                    active_tile.pos = npos
                    continue
                else:
                    if level[active_tile.pos] != None and level[active_tile.pos].type == GENERATOR:
                        rest_count += 1
                        break
                    level[active_tile.pos] = active_tile
                    active_tile = Tile(500, 0, SAND)
                    rest_count += 1

    return rest_count

with open('input') as f:
    lines = f.read().splitlines()

    level = defaultdict(lambda: None)

    min_x = min_y = 999999
    max_x = max_y = -1

    for line in lines:
        coords = list(map(lambda s: (int(s[0]), int(s[1])) , map(lambda s: s.split(',') , line.split(' -> '))))

        # find min/max
        xs = list(map(lambda c: c[0], coords))
        ys = list(map(lambda c: c[1], coords))

        min_x = min([*xs, min_x])
        max_x = max([*xs, max_x])
        min_y = min([*ys, min_y])
        max_y = max([*ys, max_y])

        # set rock walls
        prev_x, prev_y = coords[0]

        for rx, ry in coords[1:]:
            if rx == prev_x:
                dir = 1 if ry > prev_y else -1
                for y in range(prev_y, ry+dir, dir): level[(rx, y)] = Tile(rx, y, ROCK)

            if ry == prev_y:
                dir = 1 if rx > prev_x else -1
                for x in range(prev_x, rx+dir, dir): level[(x, ry)] = Tile(x, ry, ROCK)

            prev_x = rx
            prev_y = ry

    level[(500, 0)] = Tile(500, 0, GENERATOR)

    # part 1
    print(simulate(deepcopy(level), max_y, detect_floor=False))

    # part 2
    print(simulate(deepcopy(level), max_y, detect_floor=True))
