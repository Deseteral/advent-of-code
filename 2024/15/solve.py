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
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0),
]

move_vec = ['^', '>', 'v', '<']


def widen_level(level):
    rl: list[list[str]] = []
    for y in range(len(level[0])):
        ll = []
        for x in range(len(level)):
            c = level[y][x]
            if c == '@':
                ll += ['@', '.']
            elif c == 'O':
                ll += ['[', ']']
            else:
                ll += [c, c]
        rl.append(ll)
    return rl


def at_pos(v, level) -> str | None:
    w = len(level[0])
    h = len(level)
    if v.x < 0 or v.y < 0 or v.x >= w or v.y >= h:
        return None
    return level[v.y][v.x]


def move_box(pos, dir, level):
    assert at_pos(pos, level) == 'O'
    npos = pos + dir

    if at_pos(npos, level) == '#':
        return
    if at_pos(npos, level) == 'O':
        move_box(npos, dir, level)
    if at_pos(npos, level) == '.':
        level[pos.y][pos.x] = '.'
        level[npos.y][npos.x] = 'O'


def main(input_file, _):
    lines, moves = input_file.read().split('\n\n')
    lines = lines.splitlines()
    moves = ''.join(moves.splitlines())

    # Part 1
    level = [[c for c in line] for line in lines]
    w = len(level[0])
    h = len(level)

    position = None
    for y in range(h):
        for x in range(w):
            if at_pos(Vec2(x, y), level) == '@':
                position = Vec2(x, y)
                level[y][x] = '.'

    for move in moves:
        dir = neighbour_dir[move_vec.index(move)]
        npos = position + dir

        if at_pos(npos, level) == '#':
            continue

        if at_pos(npos, level) == 'O':
            move_box(npos, dir, level)

        if at_pos(npos, level) == '.':
            position = npos

    total1 = 0
    for y in range(h):
        for x in range(w):
            if at_pos(Vec2(x, y), level) in 'O[':
                total1 += y * 100 + x

    print(total1)

    # Part 2
    level = [[c for c in line] for line in lines]
    level: list[list[str]] = widen_level(level)
    w = len(level[0])
    h = len(level)

    def find_wide_boxes(pos, dir):
        apos = pos
        bpos = pos + neighbour_dir[move_vec.index('<' if at_pos(apos, level) == ']' else '>')]

        napos = apos + dir
        nbpos = bpos + dir

        tna = at_pos(napos, level)
        tnb = at_pos(nbpos, level)

        if tna == '#' or tnb == '#':
            return None

        network = {apos: at_pos(apos, level), bpos: at_pos(bpos, level)}
        if napos != bpos and nbpos != apos and tna in '[]':
            fb = find_wide_boxes(napos, dir)
            if fb is None:
                return None
            network = network | fb
        if tnb in '[]':
            fb = find_wide_boxes(nbpos, dir)
            if fb is None:
                return None
            network = network | fb

        return network

    def move_wide_box(pos, dir):
        network = find_wide_boxes(pos, dir)

        if network is None:
            return

        for pos in network.keys():
            level[pos.y][pos.x] = '.'

        for pos in network.keys():
            c = network[pos]
            npos = pos + dir
            level[npos.y][npos.x] = c

    position = None
    for y in range(h):
        for x in range(w):
            if at_pos(Vec2(x, y), level) == '@':
                position = Vec2(x, y)
                level[y][x] = '.'
    assert position is not None

    for move in moves:
        dir = neighbour_dir[move_vec.index(move)]
        npos = position + dir

        if at_pos(npos, level) == '#':
            continue

        if at_pos(npos, level) in '[]':
            move_wide_box(npos, dir)

        if at_pos(npos, level) == '.':
            position = npos

    total2 = 0
    for y in range(h):
        for x in range(w):
            if at_pos(Vec2(x, y), level) in 'O[':
                total2 += y * 100 + x

    print(total2)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
