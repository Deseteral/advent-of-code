#!/usr/local/bin/python3
import sys
from functools import cache


def main(input_file, _):
    lines = input_file.read().split('\n\n')
    towels = lines[0].split(', ')
    designs = lines[1].splitlines()

    @cache
    def count_arrangements(design):
        if len(design) == 0:
            return 1

        count = 0
        for l in range(len(design), 0, -1):
            subdesign = design[:l]
            if subdesign in towels:
                count += count_arrangements(design[l:])

        return count

    possible_count = 0
    all_possible_count = 0
    for d in designs:
        arrangements = count_arrangements(d)
        if arrangements > 0:
            possible_count += 1
            all_possible_count += arrangements

    print(possible_count)
    print(all_possible_count)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
