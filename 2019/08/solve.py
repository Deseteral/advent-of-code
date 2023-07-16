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
    line = file.read().splitlines()[0]

    w = 25
    h = 6
    s = w * h
    layer_count = int(len(line) / s)

    layers = []
    for idx in range(0, layer_count):
        start_idx = idx * s
        layers.append(line[start_idx : start_idx+s])

    # part 1
    counters = []
    for layer in layers:
        counters.append(Counter(layer))

    best_layer_idx = 0
    best_layer_zero_count = counters[0]['0']
    for idx in range(1, layer_count):
        zero_count = counters[idx]['0']
        if zero_count < best_layer_zero_count:
            best_layer_zero_count = zero_count
            best_layer_idx = idx

    best_layer = counters[best_layer_idx]
    print(best_layer['1'] * best_layer['2'])

    # part 2
    image = [['n' for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            idx = x + w * y
            for layer in layers:
                if layer[idx] == '2':
                    continue
                else:
                    image[y][x] = '.' if layer[idx] == '0' else '#'
                    break

    for line in image: print(''.join(line))

if __name__ == '__main__': main()
