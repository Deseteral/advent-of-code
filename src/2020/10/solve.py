#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools

with open('input') as f:
    adapters = [int(x) for x in f.read().splitlines()]
    built_in = max(adapters) + 3
    adapters.append(built_in)
    adapters.append(0)
    adapters = sorted(adapters)

    # part 1
    differences = ''
    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        differences += f"{diff}"

    c = Counter(differences)
    print(f"differences multiplied: {c['1'] * c['3']}")

    # part 2
    possible_connections = defaultdict(lambda: 0)
    possible_connections[0] = 1
    for curr_adapter in adapters[1:]:
        possible_connections[curr_adapter] = possible_connections[curr_adapter-1] + possible_connections[curr_adapter-2] + possible_connections[curr_adapter-3]

    print(f"possible arrangements: {possible_connections[built_in]}")
