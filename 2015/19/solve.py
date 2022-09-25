#!/usr/local/bin/python3
import re

with open('input') as f:
    lines = f.read().splitlines()

    rules = []
    results = []

    for line in lines:
        if line == '': break
        [a, b] = line.split(' => ')
        rules.append((a, b))

    molecule = lines[-1]

    # part 1
    unique_keys = list(set(map(lambda x: x[0], rules)))
    next_molecules = []

    for match in re.compile('|'.join(unique_keys)).finditer(molecule):
        src_ml = match.group(0)
        trg_mls = list(map(lambda r: r[1], filter(lambda r: r[0] == src_ml, rules)))
        (s, e) = match.span()

        for trg in trg_mls:
            nm = molecule[:s] + trg + molecule[e:]
            next_molecules.append(nm)

    distinct_molecules_count = len(set(next_molecules))
    print('distinct_molecules_count: ', distinct_molecules_count)

    # part 2
    longest_rules = sorted(rules, key=lambda r: -len(r[1]))

    m = molecule
    steps = 0
    done = False

    while not done:
        for src, trg in longest_rules:
            next_m = m.replace(trg, src, 1)

            if next_m != m:
                m = next_m
                steps += 1

            if m == 'e':
                done = True
                break

    print('steps: ', steps)
