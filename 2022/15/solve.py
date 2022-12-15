#!/usr/local/bin/python3
import re

def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

with open('input') as f:
    lines = f.read().splitlines()

    # parsing
    sensors = []

    for line in lines:
        sx, sy, bx, by = map(int, re.match(r"^Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)$", line).groups())
        sensors.append((
            (sx, sy),
            (bx, by),
            distance((bx, by), (sx, sy)),
        ))

    # part 1
    target_row = 2000000
    covered_tiles = set()

    for s in sensors:
        sp, bp, dist = s
        fy = sp[1] - dist
        ty = sp[1] + dist

        if not target_row in range(fy, ty+1):
            continue

        ll = dist - abs(sp[1] - target_row)
        fx = sp[0] - ll
        tx = sp[0] + ll

        for xx in range(fx, tx+1):
            pos = (xx, target_row)
            if pos != sp and pos != bp:
                covered_tiles.add(xx)

    print(len(covered_tiles))

    # part 2
    sensor_borders = set()
    allowed_range = range(0, 4000000 + 1)

    for s in sensors:
        sp, bp, dist = s
        fy = sp[1] - dist
        ty = sp[1] + dist

        for yy in range(max(fy, allowed_range.start), min(ty+1, allowed_range.stop)):
            ll = dist - abs(sp[1] - yy)
            fx = sp[0] - ll - 1
            tx = sp[0] + ll + 1

            if fx in allowed_range: sensor_borders.add((fx, yy))
            if tx in allowed_range: sensor_borders.add((tx, yy))

        if fy+1 in allowed_range: sensor_borders.add((sp[0], fy+1))
        if ty+1 in allowed_range: sensor_borders.add((sp[0], ty+1))

    for pp in sensor_borders:
        is_out_of_range_for_all_sensors = True

        for sp, bp, dist in sensors:
            if pp == sp or pp == bp or distance(pp, sp) < dist:
                is_out_of_range_for_all_sensors = False
                break

        if is_out_of_range_for_all_sensors:
            print((pp[0] * 4000000) + pp[1])
            break
