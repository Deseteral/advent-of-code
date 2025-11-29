#!/usr/local/bin/python3
import sys
from collections import defaultdict
from functools import cmp_to_key

def get_middle_element(l):
    return l[int(len(l) / 2)]


def main(input_file):
    sections = input_file.read().split('\n\n')

    adj = defaultdict(list)
    for line in sections[0].splitlines():
        a, b = line.split('|')
        adj[int(a)].append(int(b))

    def compare_func(x, y):
        return -1 if y in adj[x] else 1

    total1 = 0
    total2 = 0
    for line in sections[1].splitlines():
        pages = list(map(int, line.split(',')))
        pages_sorted = sorted(pages, key=cmp_to_key(compare_func))

        if pages == pages_sorted:
            total1 += get_middle_element(pages)
        else:
            total2 += get_middle_element(pages_sorted)

    print(total1)
    print(total2)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
