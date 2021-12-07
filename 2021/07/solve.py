#!/usr/local/bin/python3
import statistics

def series_sum(n):
    return int((n * (n + 1)) / 2)

with open('input') as f:
    lines = f.read().splitlines()
    positions = list(map(lambda x: int(x), lines[0].split(',')))

    target = int(statistics.median(positions))
    simple_cost = sum([abs(pos - target) for pos in positions])
    print(f"simple_cost {simple_cost}")

    cost = min([
        sum([series_sum(abs(pos - target)) for pos in positions])
        for target in range(min(positions), max(positions) + 1)
    ])
    print(f"cost {cost}")
