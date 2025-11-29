#!/usr/local/bin/python3

def execute(lines, a, b):
    pc = 0
    reg = {'a': a, 'b': b}

    while pc < len(lines):
        line = lines[pc]
        op = line[:3]
        arg = line[4:]

        if op == 'hlf':
            reg[arg] = int(reg[arg] / 2)
            pc += 1

        if op == 'tpl':
            reg[arg] = int(reg[arg] * 3)
            pc += 1

        if op == 'inc':
            reg[arg] = int(reg[arg] + 1)
            pc += 1

        if op == 'jmp':
            pc += int(arg)

        if op == 'jie':
            r, offset = arg.split(', ')
            pc += int(offset) if (reg[r] % 2 == 0) else 1

        if op == 'jio':
            r, offset = arg.split(', ')
            pc += int(offset) if (reg[r] == 1) else 1

    print(reg['b'])

with open('input') as f:
    lines = f.read().splitlines()

    execute(lines, 0, 0)
    execute(lines, 1, 0)
