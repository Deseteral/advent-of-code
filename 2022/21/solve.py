#!/usr/local/bin/python3

def find_ident(name, lines):
    for line in lines:
        if line.startswith(name):
            return line.split(': ')[1]

def resolve_ident(name, lines):
    i = find_ident(name, lines)

    if i.isnumeric():
        return i

    a, op, b = i.split(' ')
    return f"({resolve_ident(a, lines)} {op} {resolve_ident(b, lines)})"

def resolve_ident_with_var_humn(name, lines):
    if name == 'humn':
        return 'humn'

    i = find_ident(name, lines)

    if i.isnumeric():
        return i

    a, op, b = i.split(' ')

    a = resolve_ident_with_var_humn(a, lines)
    b = resolve_ident_with_var_humn(b, lines)

    if 'humn' not in a:
        a = int(eval(a))

    if 'humn' not in b:
        b = int(eval(b))

    equation = f"({a} {op} {b})"

    if 'humn' not in equation:
        equation = int(eval(equation))

    return f"{equation}"

with open('input') as f:
    lines = f.read().splitlines()

    # part 1
    print(int(eval(resolve_ident('root', lines))))

    # part 2
    root = find_ident('root', lines)
    lhs, rhs = root.split(' + ')
    lhs = resolve_ident_with_var_humn(lhs, lines)
    rhs = int(eval(resolve_ident_with_var_humn(rhs, lines)))

    actual_humn = 1000000000000
    inc = 1000000000000

    while True:
        humn = actual_humn + inc
        solved = int(eval(lhs))

        if solved < rhs:
            inc = int(inc / 10)
        else:
            actual_humn += inc

        if solved == rhs:
            break

    print(actual_humn)
