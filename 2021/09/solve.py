#!/usr/local/bin/python3
import math

def get_point(x, y, level):
    if x < 0: return -1
    if x >= len(level[0]): return -1
    if y < 0: return -1
    if y >= len(level): return -1
    return level[y][x]

with open('input') as f:
    lines = f.read().splitlines()

    level = [
        [int(x) for x in line] for line in lines
    ]

    adj_points = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]

    # part 1
    low_points = []

    for y in range(0, len(level)):
        for x in range(0, len(level[y])):
            current_point = get_point(x, y, level)
            is_lowest = True

            for ax, ay in adj_points:
                nx = x + ax
                ny = y + ay
                np = get_point(nx, ny, level)
                if np == -1: continue
                if np <= current_point: is_lowest = False

            if is_lowest:
                low_points.append((current_point, (x, y)))

    risk_level = sum(map(lambda x: x[0] + 1, low_points))
    print(f"risk_level {risk_level}")

    # part 2
    basins = []

    for low_point in low_points:
        pos = low_point[1]

        basin_size = 0
        flood_map = [pos]
        visited = []

        while len(flood_map) > 0:
            cx, cy = flood_map.pop()

            if (cx, cy) in visited: continue
            visited.append((cx, cy))

            cp = get_point(cx, cy, level)
            if cp == 9 or cp == -1: continue

            basin_size += 1

            for dx, dy in adj_points:
                nx = cx + dx
                ny = cy + dy
                flood_map.append((nx, ny))

        basins.append(basin_size)

    multiplied_top_three_sizes = math.prod(sorted(basins)[-3:])
    print(f"multiplied_top_three_sizes {multiplied_top_three_sizes}")
