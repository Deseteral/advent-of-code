#!/usr/local/bin/python3
from pprint import pprint
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy
import numpy as np

def main():
    # file = open('input')
    file = open('test_input')
    lines = file.read().splitlines()

    recipes = dict()

    for line in lines:
        # products = line.split(" => ")[0].split(", ")
        # products = list(map(lambda p: [int(p.split(" ")[0]), p.split(" ")[1]], products))

        target_amount, target = line.split(' => ')[1].split(' ')
        recipes[target] = (int(target_amount), line.split(' => ')[0].replace(', ', '+').replace(' ', '*').replace('ORE', "1"))

    for k in recipes:
        recipes[k] = (recipes[k][0], '+'.join(map(lambda s: f"({s})", recipes[k][1].split('+'))))

    pprint(recipes)

    # magic = '+'.join(map(lambda s: f"({s})", recipes['FUEL'][1].split('+')))
    magic = recipes['FUEL'][1]
    pprint(magic)

    while True:
        expressions = re.findall(r"(\(\d+\*[A-Z]+\))", magic)
        # expressions = re.findall(r"(\((\d+\*[A-Z]+\+?)+\))", magic)
        for expr in expressions:
            # expr = match if isinstance(match, str) else match[0]

            idx = magic.index(expr)

            without_parens = expr[1:-1]
            amount, target = without_parens.split('*')
            amount = int(amount)

            target_amount, target_expr = recipes[target]

            times = int(math.ceil(amount / target_amount))

            next_expr = f"({times} * ({target_expr}))"

            print('')
            print(f"replace {expr} with {next_expr}")

            magic = magic[:idx] + next_expr + magic[idx+len(expr):]
            print(magic)

        if len(expressions) == 0: break

    print('')
    print(eval(magic))














    # --------------------------------------
    # # print(recipes)

    # # for r in recipes:
    # #     print(recipes[r])

    # def resolve_recipe(target_recipe):
    #     if target_recipe[1] == "ORE":
    #         return target_recipe

    #     recipe = recipes[target_recipe[1]]

    #     amount, products = recipe[1]
    #     return list(map(
    #         lambda p: resolve_recipe(target_recipe),
    #         products,
    #     ))

    # print(resolve_recipe([1, "FUEL"]))

if __name__ == '__main__': main()
