#!/usr/local/bin/python3
import sys
from collections import defaultdict
from itertools import combinations


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def scale(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Vec2({self.x} {self.y})"

    def __repr__(self):
        return f"Vec2({self.x} {self.y})"

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")

    def copy(self):
        return Vec2(self.x, self.y)

    def distance(self, to):
        return Vec2(to.x - self.x, to.y - self.y)

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __lt__(self, other):
        return False


directions = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0),
]

directions_pairs = [
    (directions[0], directions[2]),
    (directions[1], directions[3]),
]


def main(input_file, _):
    lines = input_file.read().splitlines()

    w = len(lines[0])
    h = len(lines)

    level = [[lines[y][x] for x in range(w)] for y in range(h)]

    def at_pos(pos):
        if pos.x < 0 or pos.y < 0 or pos.x >= w or pos.y >= h:
            return None
        return level[pos.y][pos.x]

    start_pos = None
    floors = set()
    walls = set()
    for y in range(h):
        for x in range(w):
            p = Vec2(x, y)
            if at_pos(p) == 'S':
                start_pos = p
                level[y][x] = '.'
            if at_pos(p) == 'E':
                level[y][x] = '.'
            if at_pos(p) == '.':
                floors.add(p)
            if at_pos(p) == '#':
                walls.add(p)

    def bfs(start):
        q = [(start, 0)]
        visited = dict()
        while len(q) > 0:
            pos, distance = q.pop(0)
            if pos in visited:
                continue
            visited[pos] = distance
            for nn in directions:
                np = pos + nn
                if np in floors:
                    q.append((np, distance + 1))
        return visited

    distance_from_start = bfs(start_pos)

    # Part 1
    total_saved = 0
    for pos in walls:
        for na, nb in directions_pairs:
            nap = pos + na
            nbp = pos + nb
            if nap in floors and nbp in floors:
                saved = abs(distance_from_start[nap] - distance_from_start[nbp]) - 2
                if saved >= 100:
                    total_saved += 1

    print(total_saved)

    # Part 2
    total_saved = 0
    for nap, nbp in combinations(floors, 2):
        distance = nap.manhattan_distance(nbp)
        if distance > 20:
            continue
        saved = abs(distance_from_start[nap] - distance_from_start[nbp]) - distance
        if saved >= 100:
            total_saved += 1

    print(total_saved)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
