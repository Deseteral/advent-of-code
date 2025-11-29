#!/usr/local/bin/python3
import functools
import math

neighbour_dir = [
    (0, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

@functools.cache
def calc_blizzards_in_time(time, initial_blizzards, w, h):
    b = initial_blizzards
    for _ in range(time):
        b = calc_blizzards(b, w, h)
    return set(map(lambda bz: bz[0], b))

@functools.cache
def calc_blizzards(blizzards, w, h):
    next_blizz = []
    for blizz_pos, blizz_dir in blizzards:
        nx = blizz_pos[0] + blizz_dir[0]
        ny = blizz_pos[1] + blizz_dir[1]

        if nx == 0: nx = w-1-1
        if ny == 0: ny = h-1-1
        if nx == w-1: nx = 1
        if ny == h-1: ny = 1

        next_blizz.append(((nx, ny), blizz_dir))
    return tuple(next_blizz)

def main():
    file = open('input')
    lines = file.read().splitlines()

    h = len(lines)
    w = len(lines[0])

    start_position = (1, 0)
    end_position = (w-2, h-1)

    # set up initial blizzards
    blizzards = []

    for yy, line in enumerate(lines):
        for xx, c in enumerate(line):
            if c == '.' or c == '#': continue

            pos = (xx, yy)
            direction = None

            if c == '>': direction = (1, 0)
            if c == '<': direction = (-1, 0)
            if c == '^': direction = (0, -1)
            if c == 'v': direction = (0, 1)

            blizzards.append((pos, direction))

    blizzards = tuple(blizzards)

    # set up walls
    walls = set()
    for x in range(0, w):
        walls.add((x, -1))
        walls.add((x, 0))
        walls.add((x, h-1))
        walls.add((x, h))
    for y in range(0, h):
        walls.add((-1, y))
        walls.add((0, y))
        walls.add((w-1, y))
        walls.add((w, y))

    walls.remove(start_position)
    walls.remove(end_position)

    # search
    queue = [(1, 0, 0)]
    visited = set((1, 0, 0))

    targets = [end_position, start_position, end_position]

    while True:
        if len(targets) == 0: break

        target = targets.pop(0)

        while len(queue) > 0:
            node = queue.pop(0)
            if node[0] == target[0] and node[1] == target[1]:
                queue = list([node])
                visited = set([node])
                break

            t = node[2] + 1
            tm = t % math.lcm(w*h)

            b = calc_blizzards_in_time(tm, blizzards, w, h)
            collision = b.union(walls)

            for nd in neighbour_dir:
                nx = node[0] + nd[0]
                ny = node[1] + nd[1]

                if (nx, ny, tm) in visited:
                    continue

                if (nx, ny) not in collision:
                    visited.add((nx, ny, tm))
                    queue.append((nx, ny, t))

        if target == end_position:
            print(queue[0][2])

if __name__ == '__main__': main()
