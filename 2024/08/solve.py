#!/usr/local/bin/python3
import sys
from collections import defaultdict
from itertools import product, repeat, permutations, count


def main(input_file):
    level = input_file.read().splitlines()

    level_width = len(level[0])
    level_height = len(level)

    def at_pos(pos: Vec2):
        return level[pos.y][pos.x]

    def is_in_bounds(pos: Vec2):
        return 0 <= pos.x < level_width and 0 <= pos.y < level_height

    antennas: defaultdict[str, list[Vec2]] = defaultdict(list)

    for y in range(level_height):
        for x in range(level_width):
            pos = Vec2(x, y)
            c = at_pos(pos)
            if c != '.':
                antennas[c].append(pos)

    unique_antinode_positions_doubled_distance = set()
    unique_antinode_positions = set()

    for antenna_type in antennas.keys():
        for (a, b) in permutations(antennas[antenna_type], 2):
            # Part 1
            antinode_pos = a + a.distance(b).scale(2)
            if is_in_bounds(antinode_pos):
                unique_antinode_positions_doubled_distance.add(antinode_pos)

            # Part 2
            for rep in count(start=1, step=1):
                antinode_pos = a + a.distance(b).scale(rep)
                if is_in_bounds(antinode_pos):
                    unique_antinode_positions.add(antinode_pos)
                else:
                    break

    print(len(unique_antinode_positions_doubled_distance))
    print(len(unique_antinode_positions))


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


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
