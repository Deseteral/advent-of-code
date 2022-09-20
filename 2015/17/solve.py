#!/usr/local/bin/python3
from collections import defaultdict

# with open('test_input') as f:
with open('input') as f:
    lines = list(map(lambda x: int(x), f.read().splitlines()))

    count = 0
    best_used_reg = defaultdict(lambda: 0)

    for n in range(1 << len(lines)):
        total = 0
        used = 0

        for k in range(0, len(lines)):
            if ((n & (1 << k)) != 0):
                total += lines[k]
                used += 1

        if total == 150:
            count += 1
            best_used_reg[used] = best_used_reg[used] + 1

    print(count)

    best_used = min(best_used_reg.keys())
    best_used_times = best_used_reg[best_used]
    print(best_used_times)
