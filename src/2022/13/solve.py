#!/usr/local/bin/python3
import math
import numpy as np
import functools

def check(a, b):
    idx = -1
    while True:
        idx += 1

        if idx >= len(a) and idx >= len(b): return 0
        if idx >= len(a): return 1
        if idx >= len(b): return -1

        e1 = a[idx]
        e2 = b[idx]

        if type(e1) is int and type(e2) is int:
            if e1 > e2: return -1
            elif e1 < e2: return 1
            else: continue

        if type(e1) is list and type(e2) is list:
            res = check(e1, e2)
            if res == 0: continue
            return res

        if type(e1) is list and type(e2) is int:
            res = check(e1, [e2])
            if res == 0: continue
            return res

        if type(e1) is int and type(e2) is list:
            res = check([e1], e2)
            if res == 0: continue
            return res

with open('input') as f:
    lines = f.read().splitlines()

    # part 1
    right_orders = []
    pair_idx = 0
    for i in range(1, len(lines), 3):
        pair_idx += 1
        a = eval(lines[i-1])
        b = eval(lines[i])
        if check(a, b) == 1: right_orders.append(pair_idx)

    print(sum(right_orders))

    # part 2
    divider_packets = ['[[2]]', '[[6]]']
    lines = [*lines, *divider_packets]
    lines = list(map(eval, filter(lambda line: len(line) > 0, lines)))
    lines = sorted(lines, key=functools.cmp_to_key(check), reverse=True)

    divider_idx = []
    for idx, line in enumerate(lines):
        ss = np.array2string(np.array(line, dtype=object))
        if ss in divider_packets:
            divider_idx.append(idx + 1)

    print(math.prod(divider_idx))
