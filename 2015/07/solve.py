#!/usr/local/bin/python3
import re
import numpy as np
from collections import defaultdict

def normalize_value(value):
    return np.array([value],dtype="uint16")[0]

def resolve_variable(var, registers):
    if var.isnumeric():
        return normalize_value(int(var))
    else:
        return registers[var]

with open('input') as f:
    lines = f.read().split('\n')

    registers = defaultdict(lambda: 0)

    for line in lines:
        ss = line.split(" -> ")
        lhs = ss[0]
        target = ss[1]

        if re.match(r"^(\d)+$", lhs):
            registers[target] = normalize_value(int(lhs))
        elif re.match(r"^(.+) (\w+) (.+)$", lhs):
            groups = re.match(r"^(.+) (\w+) (.+)$", lhs).groups()
            a = resolve_variable(groups[0], registers)
            op = groups[1]
            b = resolve_variable(groups[2], registers)

            if op == 'AND':
                registers[target] = normalize_value(a & b)
            elif op == 'OR':
                registers[target] = normalize_value(a | b)
            elif op == 'LSHIFT':
                registers[target] = normalize_value(a << b)
            elif op == 'RSHIFT':
                registers[target] = normalize_value(a >> b)

        elif re.match(r"^NOT (.)+$", lhs):
            source = resolve_variable(lhs[4:], registers)
            registers[target] = normalize_value(~source)

    print(registers)
    print(f"value of a: {registers['a']}")
