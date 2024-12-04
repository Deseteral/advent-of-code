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


def rows(matrix):
    return groups(matrix, lambda x, y: y)


def forward_diagonals(matrix):
    return groups(matrix, lambda x, y: x + y)


def backward_diagonals(matrix):
    return groups(matrix, lambda x, y: x - y)


def join_to_string(l):
    return list(map(lambda x: ''.join(x), l))


def main(input_file):
    l = input_file.read().splitlines()

    # Part 1
    count = 0
    for f in [columns, rows, forward_diagonals, backward_diagonals]:
        for ll in join_to_string(f(l)):
            count += ll.count('XMAS') + ll.count('XMAS'[::-1])

    print(count)

    # Part 2
    count_x = 0
    for y in range(1, len(l) - 1):
        for x in range(1, len(l[0]) - 1):
            if l[y][x] != 'A': continue

            fok = (
                (l[y - 1][x - 1] == 'M' and l[y + 1][x + 1] == 'S') or
                (l[y - 1][x - 1] == 'S' and l[y + 1][x + 1] == 'M')
            )
            bok = (
                (l[y - 1][x + 1] == 'M' and l[y + 1][x - 1] == 'S') or
                (l[y - 1][x + 1] == 'S' and l[y + 1][x - 1] == 'M')
            )

            if fok and bok: count_x += 1

    print(count_x)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    file = open('input' if not env_test_run else 'test_input')
    main(file)
