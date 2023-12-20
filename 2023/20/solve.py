#!/usr/local/bin/python3
import math
from collections import Counter
import itertools


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Input parsing
    modules = {}

    for line in lines:
        module_name, outputs = line.split(' -> ')
        outputs = outputs.split(', ')

        module_type = 'untyped' if module_name[0].isalnum() else module_name[0]
        if module_name == 'broadcaster':
            module_type = 'broadcaster'

        module_name = module_name if module_name[0].isalnum() else module_name[1:]

        memory = None
        if module_type == '%':
            memory = [0]
        if module_type == '&':
            memory = {}

        modules[module_name] = (module_type, outputs, memory)

    modules['rx'] = ('untyped', [], None)

    for k, v in modules.items():
        for output in v[1]:
            if modules[output][0] == '&':
                modules[output][2][k] = 0

    cycle_detection = {}
    for k, v in modules.items():
        if 'zg' in v[1]:
            cycle_detection[k] = -1

    pulses = []
    outs = []
    for iteration_idx in itertools.count(start=1, step=1):
        pulses.append((0, 'button', 'broadcaster'))

        # Part 1
        if iteration_idx == 1000 + 1:
            c = Counter(outs)
            print(c[0] * c[1])

        # Part 2
        if all([True if x != -1 else False for x in cycle_detection.values()]):
            print(math.lcm(*cycle_detection.values()))
            break

        # Process pulses
        while len(pulses) > 0:
            pulse_value, pulse_from, pulse_to = pulses[0]
            pulses = pulses[1:]

            for k in cycle_detection.keys():
                if modules['zg'][2][k] == 1 and cycle_detection[k] == -1:
                    cycle_detection[k] = iteration_idx

            outs.append(pulse_value)

            module_type, outputs, memory = modules[pulse_to]
            if module_type == '%':
                if pulse_value == 0:
                    memory[0] = abs(memory[0] - 1)  # flip
                    for o in outputs:
                        pulses.append((memory[0], pulse_to, o))

            if module_type == '&':
                memory[pulse_from] = pulse_value
                if all([True if x == 1 else False for x in memory.values()]):
                    for o in outputs:
                        pulses.append((0, pulse_to, o))
                else:
                    for o in outputs:
                        pulses.append((1, pulse_to, o))

            if module_type == 'broadcaster':
                for o in outputs:
                    pulses.append((pulse_value, pulse_to, o))


if __name__ == '__main__':
    main()
