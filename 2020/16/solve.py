#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy

def is_valid_for_rule(value, rule):
    return (rule[0][0] <= value <= rule[0][1]) or (rule[1][0] <= value <= rule[1][1])

with open('input') as f:
    line_groups = f.read().split('\n\n')

    rules = []
    for rule_def in line_groups[0].splitlines():
        l1, h1, l2, h2 = [int(x) for x in re.match(r"^.+\: (\d+)\-(\d+) or (\d+)\-(\d+)$", rule_def).groups()]
        rule = ((l1, h1), (l2, h2))
        rules.append(rule)

    my_values = [int(x) for x in line_groups[1].splitlines()[1].split(',')]
    tickets = [[int(x) for x in line.split(',')] for line in line_groups[2].splitlines()[1:]]

    # part 1
    invalid_values = []
    valid_tickets = []

    for ticket in tickets:
        is_valid_ticket = True

        for ticket_value in ticket:
            is_valid_value = False

            for rule in rules:
                if is_valid_for_rule(ticket_value, rule):
                    is_valid_value = True
                    break

            if not is_valid_value:
                invalid_values.append(ticket_value)
                is_valid_ticket = False

        if is_valid_ticket:
            valid_tickets.append(ticket)

    print(f"sum of invalid values: {sum(invalid_values)}")

    # part 2
    skipped_columns = []
    skipped_rules = []
    departure_columns = []

    while len(departure_columns) < 6:
        for column_idx in range(20):
            if column_idx in skipped_columns: continue

            valid_rules = set([x for x in range(20)])
            for ticket in valid_tickets:
                for rule_idx, rule in enumerate(rules):
                    if not is_valid_for_rule(ticket[column_idx], rule):
                        valid_rules.discard(rule_idx)

            for skipped_rule_idx in skipped_rules:
                valid_rules.discard(skipped_rule_idx)

            if len(valid_rules) == 1:
                rule_idx = valid_rules.pop()
                skipped_columns.append(column_idx)
                skipped_rules.append(rule_idx)

                if 0 <= rule_idx <= 5:
                    departure_columns.append(column_idx)

    departure_mul = 1
    for ac in departure_columns:
        departure_mul *= my_values[ac]
    print(f"multiplication of departure values: {departure_mul}")
