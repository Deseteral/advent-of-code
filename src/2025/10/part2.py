#!/usr/local/bin/python3
import sys
import z3


def main(input_file, _):
    total = 0
    for lines in input_file.read().splitlines():
        tokens = lines.split(' ')
        buttons = tokens[1:-1]
        joltage = tokens[-1]

        o = z3.Optimize()

        buttons = list(map(lambda s: set(map(int, s[1:-1].split(','))), buttons))
        joltage = list(map(int, joltage[1:-1].split(',')))

        variables = [z3.Int(f"b_{i}") for i in range(len(buttons))]
        for v in variables: o.add(v >= 0)

        for joltage_idx, joltage_level in enumerate(joltage):
            picked_variables = []
            for button_idx, button in enumerate(buttons):
                if joltage_idx in button: picked_variables.append(variables[button_idx])
            o.add(z3.Sum(picked_variables) == joltage_level)


        o.minimize(z3.Sum(variables))
        o.check()
        model = o.model()
        total += sum(map(lambda v: model[v].as_long(), variables))

    print(total)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
