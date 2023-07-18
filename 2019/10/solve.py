#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy
import numpy as np

def main():
    file = open('input')
    # file = open('test_input')
    lines = file.read().splitlines()

    size = len(lines)

    asteroids = set()

    for y in range(size):
        for x in range(size):
            if (lines[y][x] == '#'): asteroids.add((x, y))

    sizes = []
    for current_a in asteroids:
        relative = set()

        for a in asteroids:
            if current_a == a: continue
            relative.add((a[0] - current_a[0], a[1] - current_a[1]))

        u = set()

        for r in relative:
            a = r[0]
            b = r[1]
            gcd = -1

            while gcd != 1:
                gcd = math.gcd(a, b)
                a = int(a / gcd)
                b = int(b / gcd)

            u.add((a, b))

        sizes.append(len(u))

    print(max(sizes))




if __name__ == '__main__': main()
