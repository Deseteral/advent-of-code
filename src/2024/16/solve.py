#!/usr/local/bin/python3
import sys
from collections import defaultdict


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


directions = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0),
]


def bfs(start_pos: Vec2, end_pos: Vec2, level: list[list[str]]):
    q = [(0, start_pos, Vec2(1, 0), [start_pos])]

    best_score = float('inf')
    visited_score = defaultdict(lambda: float('inf'))
    paths_with_best_score = []

    w = len(level[0])
    h = len(level)

    while len(q) > 0:
        score, position, direction, path = q.pop(0)

        if position == end_pos:
            if score < best_score:
                best_score = score
                paths_with_best_score = []
            if score == best_score:
                paths_with_best_score.append(path)
            continue

        for neighbour_dir in directions:
            neighbour_pos = position + neighbour_dir

            if neighbour_pos.x < 0 or neighbour_pos.y < 0 or neighbour_pos.x >= w or neighbour_pos.y >= h:
                continue

            neighbour_tile = level[neighbour_pos.y][neighbour_pos.x]

            if neighbour_tile == '#':
                continue

            if neighbour_dir.x == -direction.x and neighbour_dir.y == -direction.y:
                continue

            score_to_neighbour = 1 if neighbour_dir == direction else 1001
            next_score = score + score_to_neighbour

            next_path = [*path, neighbour_pos]

            if visited_score[(neighbour_pos, neighbour_dir)] < next_score:
                continue

            visited_score[(neighbour_pos, neighbour_dir)] = next_score
            q.append((next_score, neighbour_pos, neighbour_dir, next_path))

    return best_score, paths_with_best_score


def main(input_file, _):
    level = input_file.read().splitlines()
    w = len(level[0])
    h = len(level)

    start_pos = None
    end_pos = None

    for y in range(h):
        for x in range(w):
            if level[y][x] == 'S':
                start_pos = Vec2(x, y)
            elif level[y][x] == 'E':
                end_pos = Vec2(x, y)

    assert start_pos is not None
    assert end_pos is not None

    best_score, paths = bfs(start_pos, end_pos, level)
    print(best_score)

    visited = set()
    for path in paths:
        visited = visited | set(path)
    print(len(visited))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
