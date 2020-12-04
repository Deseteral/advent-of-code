#!/usr/local/bin/python3
import re
import numpy as np

def eval_expression(expression):
    if type(expression) == str:
        if ('AND' in expression) or ('OR' in expression) or ('SHIFT' in expression):
            a, op, b = expression.split(' ')

            a = resolve_variable(a)
            b = resolve_variable(b)

            if op == 'AND':
                return normalize_value(a & b)
            elif op == 'OR':
                return normalize_value(a | b)
            elif op == 'LSHIFT':
                return normalize_value(a << b)
            elif op == 'RSHIFT':
                return normalize_value(a >> b)

        elif re.match(r"^NOT (.)+$", expression):
            source = resolve_variable(expression[4:])
            return normalize_value(~source)

    return resolve_variable(expression)

def resolve_variable(name):
    global wires
    if type(name) == np.uint16:
        return name
    elif type(name) == int:
        return normalize_value(name)
    elif name.isnumeric():
        return normalize_value(int(name))
    else:
        wires[name] = eval_expression(wires[name])
        return wires[name]

def normalize_value(value):
    return np.array([value], dtype="uint16")[0]

def load_wires_from_file():
    global wires
    wires = dict()
    with open('input') as f:
        for line in f.read().splitlines():
            lhs, target = line.split(" -> ")
            wires[target] = lhs

# main
wires = dict()

load_wires_from_file()
a_value_1 = resolve_variable('a')
print(f"value of a: {a_value_1}")

load_wires_from_file()
wires['b'] = a_value_1
a_value_2 = resolve_variable('a')
print(f"value of a after override: {a_value_2}")
