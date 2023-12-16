#!/usr/local/bin/python3


def get_height(level):
    return len(level)


def get_width(level):
    return len(level[0])


def rotate_90deg(v, rotation_direction):
    x, y = v
    if rotation_direction == 1:
        return -y, x
    else:
        return y, -x


def light_travel(pos, delta, energized, visited, level):
    x, y = pos
    dx, dy = delta

    while True:
        x += dx
        y += dy

        if ((x, y), (dx, dy)) in visited:
            return energized

        visited.add(((x, y), (dx, dy)))

        if x < 0 or y < 0 or x >= get_width(level) or y >= get_height(level):
            return energized

        energized.add((x, y))

        at_pos = level[y][x]
        if at_pos == '/':
            r = 1 if abs(dy) == 1 else -1
            dx, dy = rotate_90deg((dx, dy), r)
        elif at_pos == '\\':
            r = 1 if abs(dx) == 1 else -1
            dx, dy = rotate_90deg((dx, dy), r)
        elif at_pos == '|' and abs(dx) == 1:
            energized |= light_travel((x, y), (0, -1), energized, visited, level)
            energized |= light_travel((x, y), (0, +1), energized, visited, level)
            break
        elif at_pos == '-' and abs(dy) == 1:
            energized |= light_travel((x, y), (-1, 0), energized, visited, level)
            energized |= light_travel((x, y), (+1, 0), energized, visited, level)
            break

    return energized


def main():
    file = open('input')
    level = file.read().splitlines()

    # Part 1
    print(len(light_travel((-1, 0), (1, 0), set(), set(), level)))

    # Part 2
    best = 0
    for x in range(get_width(level)):
        best = max(best, len(light_travel((x, -1), (0, 1), set(), set(), level)))
        best = max(best, len(light_travel((x, get_height(level)), (0, -1), set(), set(), level)))
    for y in range(get_height(level)):
        best = max(best, len(light_travel((-1, y), (1, 0), set(), set(), level)))
        best = max(best, len(light_travel((get_width(level), y), (-1, 0), set(), set(), level)))

    print(best)


if __name__ == '__main__':
    main()
