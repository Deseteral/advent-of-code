#!/usr/local/bin/python3
from operator import itemgetter


def get_column(cidx, level):
    return list(map(itemgetter(cidx), level))


def get_row(ridx, level):
    return level[ridx]


def get_height(level):
    return len(level)


def get_width(level):
    return len(level[0])


def count_diff(a, b):
    diff = 0
    for idx in range(len(a)):
        if a[idx] != b[idx]:
            diff += 1
    return diff


def process_level(level, expected_diff):
    total = 0
    for cidx in range(1, get_width(level)):
        diff = 0
        for i in range(0, get_width(level)):
            aidx = cidx - 1 - i
            bidx = cidx + i

            if aidx < 0 or bidx >= get_width(level):
                break

            diff += count_diff(get_column(aidx, level), get_column(bidx, level))

        if diff == expected_diff:
            total += cidx

    for ridx in range(1, get_height(level)):
        diff = 0
        for i in range(0, get_height(level)):
            aidx = ridx - 1 - i
            bidx = ridx + i

            if aidx < 0 or bidx >= get_height(level):
                break

            diff += count_diff(get_row(aidx, level), get_row(bidx, level))

        if diff == expected_diff:
            total += (ridx * 100)
    return total


def main():
    file = open('input')
    levels = [x.split('\n') for x in file.read().split('\n\n')]

    print(sum(map(lambda level: process_level(level, 0), levels)))
    print(sum(map(lambda level: process_level(level, 1), levels)))


if __name__ == '__main__':
    main()
