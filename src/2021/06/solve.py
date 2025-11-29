#!/usr/local/bin/python3
from collections import Counter

def calculate_total_count(entities):
    return sum(map(lambda x: x[1], entities))

with open('input') as f:
    lines = f.read().splitlines()

    c = Counter(list(map(
        lambda x: int(x),
        lines[0].split(',')
    )))

    entities = []
    for key in c.keys():
        entities.append((key, c[key]))

    for day in range(1, 256 + 1):
        to_add = 0

        for i in range(0, len(entities)):
            days, count = entities[i]
            days -= 1

            if days == -1:
                days = 6
                to_add += count

            entities[i] = (days, count)

        if to_add > 0: entities.append((8, to_add))

        if day == 80:
            print(f"after 80 days {calculate_total_count(entities)}")
        if day == 256:
            print(f"after 256 days {calculate_total_count(entities)}")
