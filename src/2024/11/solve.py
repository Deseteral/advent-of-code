#!/usr/local/bin/python3
import sys
from collections import defaultdict


def main(input_file):
    line = input_file.read().splitlines()[0].split(' ')

    stones = defaultdict(lambda: 0)
    for stone in line:
        stones[stone] += 1

    for step in range(75):
        next_stones = defaultdict(lambda: 0)
        for stone in stones.keys():
            if stone == '0':
                next_stones['1'] += stones['0']
            elif len(stone) % 2 == 0:
                half = len(stone) // 2
                a = str(int(stone[:half]))
                b = str(int(stone[half:]))
                next_stones[a] += stones[stone]
                next_stones[b] += stones[stone]
            else:
                a = str(int(stone) * 2024)
                next_stones[a] += stones[stone]
        stones = next_stones

        if step == 24:
            print(sum(stones.values()))

    print(sum(stones.values()))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
