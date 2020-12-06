#!/usr/local/bin/python3
from collections import Counter

def sum_of_anyone(lines):
    groups = [""]
    for line in lines:
        if line != '':
            groups[-1] += line
        else:
            groups.append('')

    count = 0
    for g in groups:
        unique = ''.join(set(g))
        count += len(unique)

    print(count)

def sum_of_everyone(lines):
    groups = [Counter(lines[0])]
    i = 1
    while i < len(lines):
        line = lines[i]
        if line != '':
            groups[-1] &= Counter(line)
        else:
            i += 1
            groups.append(Counter(lines[i]))

        i += 1

    count = 0
    for g in groups:
        count += len(g.values())

    print(count)

with open('input') as f:
    lines = f.read().splitlines()

    sum_of_anyone(lines)
    sum_of_everyone(lines)
