#!/usr/local/bin/python3
import re
import sys

import math


def main(input_file, _):
    lines = input_file.read().splitlines()

    w = 101
    h = 103

    robots = []
    for line in lines:
        px, py, vx, vy = map(int, re.match(r"^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$", line).groups())
        robots.append((px, py, vx, vy))

    # q0 | q1
    # q2 | q3
    left_q = range(0, (w // 2))
    right_q = range((w // 2) + 1, w)
    top_q = range(0, (h // 2))
    bottom_q = range((h // 2) + 1, h)

    time_end = w * h
    max_q_count = 0
    max_q_count_time = None

    for time in range(1, time_end + 1):
        q_count = [0, 0, 0, 0]

        for idx, (px, py, vx, vy) in enumerate(robots):
            nx = (px + vx) % w
            ny = (py + vy) % h
            robots[idx] = (nx, ny, vx, vy)

        for px, py, _, _ in robots:
            if px in left_q and py in top_q:
                q_count[0] += 1
            if px in right_q and py in top_q:
                q_count[1] += 1
            if px in left_q and py in bottom_q:
                q_count[2] += 1
            if px in right_q and py in bottom_q:
                q_count[3] += 1

        if time == 100:
            print(math.prod(q_count))

        for q_idx in range(4):
            if q_count[q_idx] > max_q_count:
                max_q_count = q_count[q_idx]
                max_q_count_time = time

    print(max_q_count_time)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
