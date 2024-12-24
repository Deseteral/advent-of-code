#!/usr/local/bin/python3
import sys


def main(input_file, _):
    starting_values, wires = input_file.read().split('\n\n')

    values = dict()
    for value in starting_values.splitlines():
        a, b = value.split(': ')
        b = int(b)
        values[a] = b

    z_keys = []
    for wire in wires.splitlines():
        a, b = wire.split(' -> ')
        a = tuple(a.split(' '))
        values[b] = a
        if b[0] == 'z':
            z_keys.append(b)
    z_keys.sort()

    def get_value(key):
        v = values[key]
        if type(v) is int:
            return v
        else:
            a, op, b = v
            a = get_value(a)
            b = get_value(b)
            if op == 'AND':
                return a & b
            elif op == 'OR':
                return a | b
            elif op == 'XOR':
                return a ^ b

    out = ''
    for key in reversed(z_keys):
        out += str(get_value(key))

    print(int(out, 2))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
