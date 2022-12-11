#!/usr/local/bin/python3
import math
from copy import deepcopy

class Monkey:
    def __init__(self):
        self.items = None
        self.operation_fn_str = None
        self.test_target = {}
        self.divisor = None
        self.inspection_count = 0

def sim_round(monkeys, can_cope):
    smallest_common_multiple = math.prod(list(map(lambda m: m.divisor, monkeys)))

    for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.inspection_count += 1
                item = (lambda old: eval(monkey.operation_fn_str))(item)

                if can_cope:
                    item = int(math.floor(item / 3))
                else:
                    item %= smallest_common_multiple

                target = monkey.test_target[item % monkey.divisor == 0]
                monkeys[target].items.append(item)

def calc_monkey_business(monkeys):
    most_active = list(map(lambda m: m.inspection_count, monkeys))
    most_active.sort(reverse=True)
    return most_active[0] * most_active[1]

with open('input') as f:
    lines = f.read().splitlines()

    # parsing
    monkeys = []
    m = Monkey()
    for line in lines:
        if line == '':
            monkeys.append(m)
            m = Monkey()
            continue

        if line.startswith('  Starting items'):
            m.items = list(map(lambda x: int(x), line.split(': ')[1].split(', ')))
        if line.startswith('  Operation'):
            m.operation_fn_str = line.split(' = ')[1]
        if line.startswith('  Test'):
            m.divisor = int(line.split(' ')[-1])
        if line.startswith('    If true'):
            m.test_target[True] = int(line.split(' ')[-1])
        if line.startswith('    If false'):
            m.test_target[False] = int(line.split(' ')[-1])

    # part 1
    m1 = deepcopy(monkeys)
    for roundNo in range(0, 20):
        sim_round(monkeys=m1, can_cope=True)
    print(calc_monkey_business(m1))

    # part 2
    m2 = deepcopy(monkeys)
    for roundNo in range(0, 10000):
        sim_round(monkeys=m2, can_cope=False)
    print(calc_monkey_business(m2))
