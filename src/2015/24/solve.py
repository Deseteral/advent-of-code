#!/usr/local/bin/python3
import math
import itertools

def find_balance(nums, group_count):
    per_group = int(sum(nums) / group_count)

    max_present_count_in_front = len(nums) - (group_count-1)
    for r in range(1, max_present_count_in_front+1):
        combinations = itertools.combinations(nums, r)
        correct_combinations = list(filter(lambda x: sum(x) == per_group, combinations))

        if len(correct_combinations) == 0: continue

        correct_combinations = list(map(lambda x: (x, math.prod(x)), correct_combinations))
        correct_combinations.sort(key=lambda t: t[1])
        print(correct_combinations[0][1])
        break

with open('input') as f:
    lines = f.read().splitlines()
    nums = list(map(lambda x: int(x), lines))

    find_balance(nums, group_count=3)
    find_balance(nums, group_count=4)
