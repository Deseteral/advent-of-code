#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

with open('input') as f:
    arrival_time, buses = f.read().splitlines()
    arrival_time = int(arrival_time)
    buses = [x if x == "x" else int(x) for x in buses.split(",")]

    # part 1
    best_id = math.inf
    best_time = math.inf
    for bus in buses:
        if bus == 'x': continue
        next_time = bus * (math.floor(arrival_time / bus) + 1)
        if best_time > next_time:
            best_time = next_time
            best_id = bus
    ans1 = best_id * (best_time - arrival_time)
    print(f"ans1 {ans1}")

    # part 2
    m = []
    r = []
    for i in range(len(buses)):
        bus = buses[i]
        if bus == 'x': continue
        m.append(bus)
        r.append(bus - i)

    ans2 = chinese_remainder(m,r)
    print(f"ans2 {ans2}")
