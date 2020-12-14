#!/usr/local/bin/python3
import re
import math
from collections import defaultdict

def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation

def get_products_value(products_amount):
    global products

    totals = [0 for x in range(len(products))]

    for i in range(len(products)):
        totals[i] += (products[i][0] * products_amount[i])
        totals[i] += (products[i][1] * products_amount[i])
        totals[i] += (products[i][2] * products_amount[i])
        totals[i] += (products[i][3] * products_amount[i])

    print(totals)

    value = 1
    for i in map(lambda x: x if x > 0 else 0, totals):
        value *= i

    return value


products = []

with open('input') as f:
    lines = f.read().splitlines()

    for line in lines:
        groups = re.match(r"^(\w+)\: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$", line).groups()

        name = groups[0]
        features = [int(x) for x in groups[1:-1]]

        products.append(features)

    permutations = list(sums(len(products), 100))
    best_value = -1
    for p in permutations:
        best_value = max(get_products_value(p), best_value)

    print(best_value)
