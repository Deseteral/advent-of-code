#!/usr/local/bin/python3
from collections import defaultdict
from collections import namedtuple

Point = namedtuple("Point", "x y z")


def point_move_down(point, by):
    x, y, z = point
    return Point(x, y, z - by)


def brick_move_down(brick, tallmap):
    a, b = brick
    max_z = -1
    for y in range(a.y, b.y + 1):
        for x in range(a.x, b.x + 1):
            max_z = max(tallmap[(x, y)], max_z)
    diff = max(a.z - max_z - 1, 0)
    return (point_move_down(a, diff), point_move_down(b, diff)), diff


def apply_gravity(bricks):
    tallmap = defaultdict(lambda: 0)
    next_bricks = []

    move_down_count = 0

    for brick_idx in range(len(bricks)):
        next_brick, move_down_diff = brick_move_down(bricks[brick_idx], tallmap)
        next_bricks.append(next_brick)

        if move_down_diff > 0:
            move_down_count += 1

        a, b = next_brick
        for y in range(a.y, b.y + 1):
            for x in range(a.x, b.x + 1):
                tallmap[(x, y)] = b.z

    return next_bricks, move_down_count


def main():
    file = open('input')
    lines = file.read().splitlines()

    bricks = []

    for line in lines:
        a, b = line.split('~')
        a = Point(*[int(x) for x in a.split(',')])
        b = Point(*[int(x) for x in b.split(',')])

        bricks.append((a, b))

    # Sort by first point's Z-axis
    bricks = sorted(bricks, key=lambda brick: brick[0].z)

    # Apply gravity
    bricks = apply_gravity(bricks)[0]

    # Single brick desintegration
    desintegration_safe = 0
    total_annihilation = 0
    for brick_idx in range(len(bricks)):
        nbs = bricks[:brick_idx] + bricks[brick_idx + 1:]
        _, move_down_count = apply_gravity(nbs)

        if move_down_count == 0:
            desintegration_safe += 1

        total_annihilation += move_down_count

    print(desintegration_safe)
    print(total_annihilation)


if __name__ == '__main__':
    main()
