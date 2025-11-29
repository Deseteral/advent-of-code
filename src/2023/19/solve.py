#!/usr/local/bin/python3
import math
from copy import deepcopy


def part1(input_content):
    workflows_def, parts_def = input_content.split('\n\n')

    src = ''
    workflows_def = workflows_def.replace('in', 'entry_point')

    for workflow_def in workflows_def.splitlines():
        method_name, body = workflow_def.split('{')
        body = body[:-1]

        condition_statements = body.split(',')

        src += f"def {method_name}(part):\n"
        src += '  x,m,a,s = part\n'

        for condition_statement in condition_statements[:-1]:
            condition, then_method_name = condition_statement.split(':')
            src += f"  if {condition}:\n"
            src += f"    {then_method_name}(part)\n"
            src += f"    return\n"

        src += f"  {condition_statements[-1]}(part)\n"
        src += '\n'

    src += 'entry_point(part)\n'

    parts = []
    for part_def in parts_def.split('\n'):
        part_attributes = tuple(map(int, map(lambda x: x[2:], part_def[1:-1].split(','))))
        parts.append(part_attributes)

    accepted_parts = []

    for part in parts:
        exec(src, {'part': part, 'A': accepted_parts.append, 'R': lambda _: None})

    print(sum(map(sum, accepted_parts)))


def part2(input_content):
    methods = {}

    for workflow_def in input_content.split('\n\n')[0].splitlines():
        mn, body = workflow_def.split('{')
        body = body[:-1]

        conditions_def = body.split(',')

        cond = []
        for c in conditions_def[:-1]:
            a, b = c.split(':')
            iden = 'xmas'.index(a[0])
            oper = a[1]
            num = int(a[2:])
            cond.append(((iden, oper, num), b))

        method = (cond, conditions_def[-1])
        methods[mn] = method

    def check_range(method_name, part_range):
        if method_name == 'R':
            return 0

        if method_name == 'A':
            return math.prod(map(lambda r: r[1] - r[0] + 1, part_range))

        m = methods[method_name]

        conditions = m[0]
        default_condition = m[1]

        count = 0
        for condition in conditions:
            (attr_idx, operator, value), next_method = condition
            pr_min, pr_max = part_range[attr_idx]

            if operator == '<':
                if pr_min < value:
                    next_part_range = deepcopy(part_range)
                    next_part_range[attr_idx] = [pr_min, (value - 1)]
                    count += check_range(next_method, next_part_range)
                if pr_max >= value:
                    part_range[attr_idx] = [value, pr_max]

            if operator == '>':
                if pr_max > value:
                    next_part_range = deepcopy(part_range)
                    next_part_range[attr_idx] = [(value + 1), pr_max]
                    count += check_range(next_method, next_part_range)
                if pr_min <= value:
                    part_range[attr_idx] = [pr_min, value]

        count += check_range(default_condition, deepcopy(part_range))
        return count

    initial_part_range = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]
    print(check_range('in', deepcopy(initial_part_range)))


def main():
    input_content = open('input').read()
    part1(input_content)
    part2(input_content)


if __name__ == '__main__':
    main()
