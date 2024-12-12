#!/usr/local/bin/python3
import sys


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
        return f"({self.x} {self.y})"

    def __repr__(self):
        return f"({self.x} {self.y})"

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")

    def copy(self):
        return Vec2(self.x, self.y)

    def distance(self, to):
        return Vec2(to.x - self.x, to.y - self.y)


neighbour_dir = [
    Vec2(0, -1),
    Vec2(0, 1),
    Vec2(-1, 0),
    Vec2(1, 0),
]


class Region:
    def __init__(self, char, tiles, area, perimeter, vertex_count):
        self.char = char
        self.tiles = tiles
        self.area = area
        self.perimeter = perimeter
        self.vertex_count = vertex_count


def main(input_file):
    level = input_file.read().splitlines()
    w = len(level[0])
    h = len(level)

    def at_pos(v):
        if v.x < 0 or v.y < 0 or v.x >= w or v.y >= h:
            return None
        return level[v.y][v.x]

    all_tiles = set()
    for y in range(h):
        for x in range(w):
            all_tiles.add(Vec2(x, y))

    def explore_region_bfs(start):
        region_type = at_pos(start)
        perimeter = 0

        q = [start]
        visited = set()

        while len(q) > 0:
            pos = q.pop(0)
            if pos in visited:
                continue
            visited.add(pos)

            for n in neighbour_dir:
                nn = pos + n

                if at_pos(nn) is None:
                    perimeter += 1
                    continue

                if at_pos(nn) == region_type:
                    q.append(nn)
                else:
                    perimeter += 1

        return Region(region_type, visited, len(visited), perimeter, None)

    regions = []
    explored_region_tiles = set()
    while len(all_tiles) > len(explored_region_tiles):
        unexplored = all_tiles - explored_region_tiles
        region = explore_region_bfs(next(iter(unexplored)))
        regions.append(region)
        explored_region_tiles = explored_region_tiles.union(region.tiles)

    lookup = [
        (Vec2(0, -1), Vec2(1, -1), Vec2(1, 0)),
        (Vec2(1, 0), Vec2(1, 1), Vec2(0, 1)),
        (Vec2(0, 1), Vec2(-1, 1), Vec2(-1, 0)),
        (Vec2(-1, 0), Vec2(-1, -1), Vec2(0, -1)),
    ]

    for region in regions:
        region.vertex_count = 0
        c = region.char
        for pos in region.tiles:
            for p1, p2, p3 in lookup:
                pp1 = pos + p1
                pp2 = pos + p2
                pp3 = pos + p3
                is_concave_vertex = (at_pos(pp1) == c and at_pos(pp3) == c and at_pos(pp2) != c)
                is_convex_vertex = (at_pos(pp1) != c and at_pos(pp3) != c)
                if is_concave_vertex or is_convex_vertex:
                    region.vertex_count += 1

    print(sum(map(lambda r: r.area * r.perimeter, regions)))
    print(sum(map(lambda r: r.area * r.vertex_count, regions)))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
