#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy

rules = {}
patch_rules_with_loops = False

def rule11(a, b, level):
    if level == 0:
        return f"({a}{b})?"
    else:
        return f"({a}{rule11(a, b, level - 1)}{b})?"

def resolve_rule(rule_num):
    global rules
    global patch_rules_with_loops
    val = rules[rule_num]

    if patch_rules_with_loops:
        if rule_num == '8':
            return f"({resolve_rule('42')})+"
        if rule_num == '11':
            a = resolve_rule('42')
            b = resolve_rule('31')
            return f"({a}{rule11(a, b, 5)}{b})"

    if '|' in val:
        l, r = val.split(' | ')
        lp = ''.join(map(resolve_rule, l.split(' ')))
        rp = ''.join(map(resolve_rule, r.split(' ')))
        return f"({lp}|{rp})"
    elif ' ' in val:
        ps = ''.join(map(resolve_rule, val.split(' ')))
        return f"({ps})"
    elif '"' in val:
        return val[1]
    else:
        return resolve_rule(val)


with open('input') as f:
    rulelines, lines = f.read().split('\n\n')
    rulelines = rulelines.splitlines()
    lines = lines.splitlines()

    for ruleline in rulelines:
        rule_num, rule = ruleline.split(': ')
        rules[rule_num] = rule

    # part 1
    pattern = f"^{resolve_rule('0')}$"
    count1 = 0
    for line in lines:
        if re.match(pattern, line): count1 += 1
    print(f"count part 1: {count1}")

    # part 2
    patch_rules_with_loops = True
    pattern = f"^{resolve_rule('0')}$"
    count2 = 0
    for line in lines:
        if re.match(pattern, line): count2 += 1
    print(f"count part 2: {count2}")
