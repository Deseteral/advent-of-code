#!/usr/local/bin/python3
import json

with open('input') as f:
    lines = f.read().splitlines()

    total_1 = 0
    total_2 = 0
    for line in lines:
        a = line
        b = bytes(line[1:-1], "utf-8").decode("unicode_escape")
        c = json.dumps(line)

        total_1 += (len(a) - len(b))
        total_2 += (len(c) - len(a))

    print(f"total_1 {total_1}")
    print(f"total_2 {total_2}")
