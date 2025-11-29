#!/usr/local/bin/python3
from collections import namedtuple
import itertools
from sympy import Symbol, solve, Eq

Point = namedtuple("Point", "x y z")


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, -C


def intersection(l1, l2):
    L1 = line(l1[0], l1[1])
    L2 = line(l2[0], l2[1])
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return Point(x, y, 0)
    else:
        return False


def calc_point_in_time(p, v, t):
    xx = p.x + (v.x * t)
    yy = p.y + (v.y * t)
    zz = p.z + (v.z * t)
    return Point(xx, yy, zz)


def main():
    file = open('input')
    input_lines = file.read().splitlines()

    # Part 1
    lines = []
    for input_line in input_lines:
        p, v = input_line.split(' @ ')
        p = Point(*[int(x) for x in p.split(', ')])
        v = Point(*[int(x) for x in v.split(', ')])

        p2 = (p.x + v.x, p.y + v.y)
        lines.append((p, p2, v))

    area_min = 200000000000000
    area_max = 400000000000000

    good_count = 0
    for l1, l2 in itertools.combinations(lines, 2):
        r = intersection(l1, l2)

        if not r:
            continue

        if r.x < area_min or r.x > area_max or r.y < area_min or r.y > area_max:
            continue

        v1 = l1[2]
        v2 = l2[2]
        is_good = True

        if not ((v1.x > 0 and r.x > l1[0].x) or (v1.x < 0 and r.x < l1[0].x)):
            is_good = False
        if not ((v2.x > 0 and r.x > l2[0].x) or (v2.x < 0 and r.x < l2[0].x)):
            is_good = False
        if not ((v1.y > 0 and r.y > l1[0].y) or (v1.y < 0 and r.y < l1[0].y)):
            is_good = False
        if not ((v2.y > 0 and r.y > l2[0].y) or (v2.y < 0 and r.y < l2[0].y)):
            is_good = False

        if is_good:
            good_count += 1

    print(good_count)

    # Part 2
    Ax, Ay, Az = Symbol('Ax'), Symbol('Ay'), Symbol('Az')
    Avx, Avy, Avz = Symbol('Avx'), Symbol('Avy'), Symbol('Avz')

    symbols = [Ax, Ay, Az, Avx, Avy, Avz]
    equations = []

    for idx, (p, _, v) in enumerate(lines[:3]):
        t = Symbol(f"t_{idx}")
        symbols.append(t)

        point_in_time = calc_point_in_time(p, v, t)

        equations.append(Eq((Ax + (Avx * t)), point_in_time.x))
        equations.append(Eq((Ay + (Avy * t)), point_in_time.y))
        equations.append(Eq((Az + (Avz * t)), point_in_time.z))

    print(sum(solve(equations, symbols)[0][:3]))


if __name__ == '__main__':
    main()
