#!/usr/local/bin/python3
import sys

neighbour_dir = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]


def bfs1(start, level, w, h):
    q = [start]
    visited = set()
    score = 0
    while len(q) > 0:
        pos = q.pop(0)
        x, y = pos
        if pos in visited:
            continue
        visited.add(pos)
        if level[y][x] == 9:
            score += 1
        for (nx, ny) in neighbour_dir:
            xx = x + nx
            yy = y + ny
            if xx < 0 or yy < 0 or xx >= w or yy >= h:
                continue
            if level[yy][xx] == level[y][x] + 1:
                q.append((xx, yy))
    return score


def bfs2(start, level, w, h):
    q = [(start,)]
    visited = set()
    completed = []
    while len(q) > 0:
        trail = q.pop(0)
        if trail in visited:
            continue
        visited.add(trail)
        pos = trail[-1]
        x, y = pos
        if level[y][x] == 9:
            completed.append(trail)
        for (nx, ny) in neighbour_dir:
            xx = x + nx
            yy = y + ny
            if xx < 0 or yy < 0 or xx >= w or yy >= h:
                continue
            if level[yy][xx] == level[y][x] + 1:
                q.append(tuple([*trail, (xx, yy)]))
    return len(completed)


def main(input_file):
    lines = input_file.read().splitlines()
    level = [[int(c) for c in line] for line in lines]
    w = len(lines[0])
    h = len(lines)

    starting_nodes = []
    for y in range(h):
        for x in range(w):
            if level[y][x] == 0:
                starting_nodes.append((x, y))

    print(sum(map(lambda node: bfs1(node, level, w, h), starting_nodes)))
    print(sum(map(lambda node: bfs2(node, level, w, h), starting_nodes)))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
