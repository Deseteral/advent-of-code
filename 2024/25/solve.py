#!/usr/local/bin/python3
import sys
from collections import defaultdict


def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))


def columns(matrix):
    return groups(matrix, lambda x, y: x)


def main(input_file, _):
    entries = list(map(lambda e: e.splitlines(), input_file.read().split('\n\n')))

    locks = []
    keys = []

    for entry in entries:
        is_lock = all(map(lambda e: e == '#', entry[0]))
        sizes = tuple(map(lambda c: c.count('#') - 1, columns(entry)))

        if is_lock:
            locks.append(sizes)
        else:
            keys.append(sizes)

    fit = 0
    for key in keys:
        for lock in locks:
            if all(map(lambda c: c <= 5, map(sum, zip(key, lock)))):
                fit += 1

    print(fit)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
