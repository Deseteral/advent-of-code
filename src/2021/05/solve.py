#!/usr/local/bin/python3
import re
import math
from collections import Counter
from shapely.geometry import LineString

def count_points_meeting_threshold(points):
    points_counter = Counter(points)
    return len(Counter(el for el in points_counter.elements() if points_counter[el] >= 2))

with open('input') as f:
    input_lines = f.read().splitlines()

    # parsing
    lines = []
    for line in input_lines:
        x1, y1, x2, y2 = list(map(
            lambda x: int(x),
            re.match(r"^(\d+)\,(\d+) -> (\d+)\,(\d+)$", line).groups()
        ))
        lines.append([(x1, y1), (x2, y2)])

    # processing
    ortho_points = []
    points = []

    for p1, p2 in lines:
        is_ortho = (p1[0] == p2[0] or p1[1] == p2[1])
        ls = LineString([p1, p2])

        prev = (-1, -1)
        for f in range(0, int(math.ceil(ls.length)) + 1):
            p = ls.interpolate(f).coords[0]
            pr = (int(round(p[0])), int(round(p[1])))
            if pr == prev: continue

            if is_ortho: ortho_points.append(pr)
            points.append(pr)

            prev = pr

    # counting
    ortho_points_count = count_points_meeting_threshold(ortho_points)
    print(f"ortho_points_count {ortho_points_count}")

    points_count = count_points_meeting_threshold(points)
    print(f"points_count {points_count}")

