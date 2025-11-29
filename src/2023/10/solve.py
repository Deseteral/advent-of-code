#!/usr/local/bin/python3
from operator import itemgetter

neighbour_dir = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

can_connect_to = {
    (0, 1): ['|', 'L', 'J'],
    (0, -1): ['|', '7', 'F'],
    (-1, 0): ['-', 'L', 'F'],
    (1, 0): ['-', 'J', '7'],
}

can_connect_dir = {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
}


def upscale_tile(rmap, x, y, tile_type):
    for yy in range(0, 3):
        for xx in range(0, 3):
            rmap[(x * 3 + xx, y * 3 + yy)] = ('.', (x, y))

    if tile_type == '.':
        return

    rmap[(x * 3 + 1, y * 3 + 1)] = ('#', (x, y))  # middle

    if tile_type == '|':
        for ny in range(0, 3):
            rmap[(x * 3 + 1, y * 3 + ny)] = ('#', (x, y))
    if tile_type == '-':
        for nx in range(0, 3):
            rmap[(x * 3 + nx, y * 3 + 1)] = ('#', (x, y))
    if tile_type == 'L':
        rmap[(x * 3 + 1, y * 3 + 0)] = ('#', (x, y))
        rmap[(x * 3 + 2, y * 3 + 1)] = ('#', (x, y))
    if tile_type == 'J':
        rmap[(x * 3 + 1, y * 3 + 0)] = ('#', (x, y))
        rmap[(x * 3 + 0, y * 3 + 1)] = ('#', (x, y))
    if tile_type == '7':
        rmap[(x * 3 + 0, y * 3 + 1)] = ('#', (x, y))
        rmap[(x * 3 + 1, y * 3 + 2)] = ('#', (x, y))
    if tile_type == 'F':
        rmap[(x * 3 + 2, y * 3 + 1)] = ('#', (x, y))
        rmap[(x * 3 + 1, y * 3 + 2)] = ('#', (x, y))


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Find start tile
    start_x, start_y = 0, 0
    for idx, line in enumerate(lines):
        if 'S' in line:
            start_y = idx
            start_x = line.index('S')

    # Replace it with an actual correct pipe
    lines[start_y] = lines[start_y][:start_x] + '7' + lines[start_y][start_x + 1:]

    # Part 1
    queue = [(start_x, start_y, 0)]
    dist_graph = [(start_x, start_y, 0)]
    visited = [(start_x, start_y)]
    while len(queue) > 0:
        px, py, dist = queue[0]
        queue = queue[1:]
        c = lines[py][px]

        for nx, ny in can_connect_dir[c]:
            xx = px + nx
            yy = py + ny
            cc = lines[yy][xx]

            if cc in can_connect_to[(nx, ny)] and (xx, yy) not in visited:
                queue.append((xx, yy, dist + 1))
                dist_graph.append((xx, yy, dist + 1))
                visited.append((xx, yy))

    print(sorted(dist_graph, key=itemgetter(2), reverse=True)[0][2])

    # Part 2
    rmap = {}
    ground_tiles = set()

    # Upscale tiles to 3x3
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if (x, y) not in visited:
                ground_tiles.add((x, y))
                upscale_tile(rmap, x, y, '.')
            else:
                upscale_tile(rmap, x, y, c)

    # Flood map from edges
    rheight = len(lines) * 3
    rwidth = len(lines[0]) * 3

    # Queue all edges
    ground_queue = []
    for y in range(rheight):
        if rmap[(0, y)][0] == '.':
            ground_queue.append((0, y))
        if rmap[(rwidth - 1, y)][0] == '.':
            ground_queue.append((rwidth - 1, y))
    for x in range(rwidth):
        if rmap[(x, 0)][0] == '.':
            ground_queue.append((x, 0))
        if rmap[(x, rheight - 1)][0] == '.':
            ground_queue.append((x, rheight - 1))

    ground_queue_visited = set()
    ground_tiles_reached = set()

    while len(ground_queue) > 0:
        x, y = ground_queue.pop()
        ground_queue_visited.add((x, y))

        tx, ty = rmap[(x, y)][1]
        if (tx, ty) in ground_tiles:
            ground_tiles_reached.add((tx, ty))

        for nx, ny in neighbour_dir:
            xx = x + nx
            yy = y + ny

            if xx < 0 or yy < 0 or xx >= rwidth or yy >= rheight:
                continue

            if (xx, yy) not in ground_queue_visited:
                if rmap[(xx, yy)][0] == '.':
                    ground_queue.append((xx, yy))

    print(len(ground_tiles - ground_tiles_reached))


if __name__ == '__main__':
    main()
