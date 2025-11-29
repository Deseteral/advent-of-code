#!/usr/local/bin/python3
import sys
from itertools import product, repeat

def eval_line(outcome, el, with_concat):
    for operators in product('+*|' if with_concat else '+*', repeat=(len(el) - 1)):
        total = el[0]
        for idx in range(len(operators)):
            op = operators[idx]
            b = el[idx + 1]
            if op == '+':
                total += b
            if op == '*':
                total *= b
            if op == '|':
                total = int(str(total) + str(b))
            if total > outcome:
                break

        if total == outcome:
            return True

    return False


def main(input_file):
    lines = input_file.read().splitlines()

    total = 0
    total_with_concat = 0
    for line in lines:
        a, b = line.split(': ')
        outcome = int(a)
        el = list(map(int, b.split(' ')))

        if eval_line(outcome, el, with_concat=False):
            total += outcome
        if eval_line(outcome, el, with_concat=True):
            total_with_concat += outcome

    print(total)
    print(total_with_concat)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
