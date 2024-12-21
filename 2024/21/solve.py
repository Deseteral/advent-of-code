#!/usr/local/bin/python3
import math
import sys
from functools import cache


def main(input_file, _):
    lines = input_file.read().splitlines()
    numeric_keypad = (
        ('7', '8', '9'),
        ('4', '5', '6'),
        ('1', '2', '3'),
        (' ', '0', 'A'),
    )
    directional_keypad = (
        (' ', '^', 'A'),
        ('<', 'v', '>'),
    )

    @cache
    def best_len_at_depth(a, b, depth):
        if depth == 1:
            return len(get_path(a, b, directional_keypad))

        path = 'A' + get_path(a, b, directional_keypad)
        length = 0
        for current_char, next_char in iter_pairs(path):
            length += best_len_at_depth(current_char, next_char, depth - 1)

        return length

    def calc_complexities(depth):
        total = 0
        for line in lines:
            numeric_code_part = int(line[:-1])

            first_directional = ''
            for current_char, next_char in iter_pairs('A' + line):
                first_directional += get_path(current_char, next_char, numeric_keypad)

            best_len = 0
            for current_char, next_char in iter_pairs('A' + first_directional):
                best_len += best_len_at_depth(current_char, next_char, depth)

            total += numeric_code_part * best_len

        return total

    # Part 1
    print(calc_complexities(2))

    # Part 2
    print(calc_complexities(25))


def get_path(from_key, to_key, keypad):
    from_key_position = get_position_of_key(from_key, keypad)
    to_key_position = get_position_of_key(to_key, keypad)
    distance = from_key_position.distance(to_key_position)

    x_sign_dir = int(math.copysign(1, distance.x))
    y_sign_dir = int(math.copysign(1, distance.y))

    moves_horizontal = abs(distance.x) * direction_moves[Vec2(x_sign_dir, 0)]
    moves_vertical = abs(distance.y) * direction_moves[Vec2(0, y_sign_dir)]

    can_move_horizontal = True
    for x in range(from_key_position.x, to_key_position.x + x_sign_dir, x_sign_dir):
        if get_key_at_position(Vec2(x, from_key_position.y), keypad) is None:
            can_move_horizontal = False

    can_move_vertical = True
    for y in range(from_key_position.y, to_key_position.y + y_sign_dir, y_sign_dir):
        if get_key_at_position(Vec2(from_key_position.x, y), keypad) is None:
            can_move_vertical = False

    # Prefer moving left, then up or down.
    if x_sign_dir == -1 and can_move_horizontal:
        return moves_horizontal + moves_vertical + 'A'
    elif can_move_vertical:
        return moves_vertical + moves_horizontal + 'A'
    else:
        return moves_horizontal + moves_vertical + 'A'


def get_position_of_key(key, keypad):
    for y in range(len(keypad)):
        for x in range(len(keypad[0])):
            if keypad[y][x] == key:
                return Vec2(x, y)
    return None


def get_key_at_position(position, keypad):
    w = len(keypad[0])
    h = len(keypad)
    if position.x < 0 or position.y < 0 or position.x >= w or position.y >= h:
        return None
    key = keypad[position.y][position.x]
    if key == ' ': return None
    return key


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

direction_moves = {
    directions[0]: '^',
    directions[1]: '>',
    directions[2]: 'v',
    directions[3]: '<',
}


def iter_pairs(s):
    return [i + j for i, j in zip(s, s[1:])]


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
