#!/usr/local/bin/python3
import sys

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")

    def copy(self):
        return Vec2(self.x, self.y)


def traverse(level, additional_obstacle = None):
    def at_pos(pos: Vec2):
        return level[pos.y][pos.x]

    level_width = len(level[0])
    level_height = len(level)

    starting_dir = Vec2(0, -1)
    direction = starting_dir.copy()

    position = None
    for idx, line in enumerate(level):
        if '^' in line:
            position = Vec2(line.index('^'), idx)

    starting_pos = position.copy()

    unique_pos = {position}
    visited = {position, direction}
    while True:
        np = position + direction
        if np.x < 0 or np.x >= level_width or np.y < 0 or np.y >= level_height:
            break

        if len(visited) > 1 and (np, direction) in visited:
            return None

        if at_pos(np) == '#' or np == additional_obstacle:
            direction = Vec2(-direction.y, direction.x)
            continue

        position = np
        unique_pos.add(position)
        visited.add((position, direction))

    return unique_pos, starting_pos


def main(input_file):
    lines = input_file.read().splitlines()

    # Part 1
    unique_pos, staring_pos = traverse(lines)
    print(len(unique_pos))

    # Part 2
    looped_count = 0
    for obstacle_pos in (unique_pos - {staring_pos}):
        outcome = traverse(lines, additional_obstacle=obstacle_pos)
        if outcome is None:
            looped_count += 1

    print(looped_count)

if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
