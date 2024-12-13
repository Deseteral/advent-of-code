#!/usr/local/bin/python3
import re
import sys

def main(input_file):
    line_groups = input_file.read().split('\n\n')

    for part in range(1, 2+1):
        total_tokens = 0

        for group in line_groups:
            lines = group.splitlines()
            ax, ay = map(int, re.match(r"^.+?(\d+).+?(\d+)$", lines[0]).groups())
            bx, by = map(int, re.match(r"^.+?(\d+).+?(\d+)$", lines[1]).groups())
            px, py = map(int, re.match(r"^.+?(\d+).+?(\d+)$", lines[2]).groups())

            if part == 2:
                px += 10000000000000
                py += 10000000000000

            # a * ax + b * bx = px
            # a * ay + b * by = py

            # ay * (a * ax + b * bx) = ay * px
            # ax * (a * ay + b * by) = ax * py

            # (a * ay * ax) + (b * bx * ay) = ay * px
            # (a * ay * ax) + (b * by * ax) = ax * py

            # (b * by * ax) - (b * bx * ay) = (ax * py) - (ay * px)

            # b * (by * ax - bx * ay) = (ax * py) - (ay * px)

            # b = ((ax * py) - (ay * px)) / (by * ax - bx * ay)
            b = ((ax * py) - (ay * px)) / (by * ax - bx * ay)
            b = int(b)

            # a * ax + b * bx = px
            # a * ax = px - (b * bx)
            # a = (px - (b * bx)) / ax
            a = (px - (b * bx)) / ax
            a = int(a)

            if (a * ax + b * bx == px) and (a * ay + b * by == py):
                total_tokens += 3 * a + b

        print(total_tokens)

if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
