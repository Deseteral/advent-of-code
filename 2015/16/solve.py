#!/usr/local/bin/python3
import re

attr = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def is_attr_passing(name, value):
    value = int(value)
    if (name in ['cats', 'trees']):
        return value > attr[name]
    elif (name in ['pomeranians', 'goldfish']):
        return value < attr[name]
    else:
        return value == attr[name]

with open('input') as f:
    lines = f.read().splitlines()

    for line in lines:
        groups = re.match(r"^Sue (\d+): (.+): (\d+), (.+): (\d+), (.+): (\d+)$", line).groups()
        (n, a, av, b, bv, c, cv) = groups
        av = int(av)
        bv = int(bv)
        cv = int(cv)

        if (attr[a] == av) and (attr[b] == bv) and (attr[c] == cv):
            print(n)

        if (is_attr_passing(a, av) and is_attr_passing(b, bv) and is_attr_passing(c, cv)):
            print(n)
