#!/usr/local/bin/python3
import re
from collections import defaultdict

with open('input') as f:
    lines = f.read().splitlines()

    stacks_a = defaultdict(lambda: [])
    stacks_b = defaultdict(lambda: [])
    moves = []

    for line in lines:
        if '[' in line:
            stack_no = -1
            for pc in range(1, len(line), 4):
                stack_no += 1
                value = line[pc]
                if value == ' ': continue
                stacks_a[stack_no].append(value)
                stacks_b[stack_no].append(value)

        if 'move' in line:
            (amount, src_stack, target_stack) = re.match(r"^move (\d+) from (\d+) to (\d+)$", line).groups()
            moves.append((int(amount), int(src_stack)-1, int(target_stack)-1))

    for move in moves:
        (amount, src_stack, target_stack) = move
        tmp_stack = []
        for _ in range(0, amount):
            stacks_a[target_stack].insert(0, stacks_a[src_stack].pop(0))
            tmp_stack.append(stacks_b[src_stack].pop(0))

        for crate in reversed(tmp_stack):
            stacks_b[target_stack].insert(0, crate)

    outcome_a = ''
    outcome_b = ''

    for i in range(0, len(stacks_a)):
        outcome_a += stacks_a[i][0]
        outcome_b += stacks_b[i][0]

    print(outcome_a)
    print(outcome_b)
