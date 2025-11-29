#!/usr/local/bin/python3

directions = [
    (0, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

def sign(n):
    if n > 0: return +1
    elif n < 0: return -1
    else: return 0

def is_touching(hx, hy, tx, ty):
    for dx, dy in directions:
        if (tx + dx) == hx and (ty + dy) == hy: return True

def simulate(lines, k):
    positions = [set() for _ in range(0, len(k))]

    for line in lines:
        direction = line[0]
        amount = int(line[2:])

        for _ in range(0, amount):
            hhx, hhy = k[0]
            if direction == 'U': hhy += 1
            if direction == 'D': hhy -= 1
            if direction == 'L': hhx -= 1
            if direction == 'R': hhx += 1

            k[0] = (hhx, hhy)

            for i in range(1, len(k)):
                hx, hy = k[i-1]
                tx, ty = k[i]

                dx = hx - tx
                dy = hy - ty

                if abs(dx) == 2 and abs(dy) == 0:
                    tx += sign(dx)
                elif abs(dy) == 2 and abs(dx) == 0:
                    ty += sign(dy)
                elif not is_touching(hx, hy, tx, ty):
                    tx += sign(dx)
                    ty += sign(dy)

                k[i] = (tx, ty)
                positions[i].add((tx, ty))

    return positions

with open('input') as f:
    lines = f.read().splitlines()

    visited = simulate(lines, [(0, 0), (0, 0)])
    print(len(visited[1]))

    visited = simulate(lines, [(0, 0) for _ in range(0, 10)])
    print(len(visited[9]))
