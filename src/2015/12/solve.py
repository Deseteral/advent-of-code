#!/usr/local/bin/python3
import json

def isnumeric(value):
    return type(value) == int or type(value) == float

def sum_number_list(values):
    return sum(list(filter(lambda x: isnumeric(x), values)))

def process_node(node, ignore_red):
    if isinstance(node, list):
        return sum_number_list(list(map(lambda x: process_node(x, ignore_red), node)))

    elif isinstance(node, dict):
        if ignore_red and "red" in node.values():
            return 0
        else:
            return process_node(list(node.values()), ignore_red)

    elif isnumeric(node):
        return node

    else:
        return 0


with open('input') as f:
    obj = json.loads(f.read())

    sum_all = process_node(obj, False)
    sum_without_red = process_node(obj, True)

    print(f"sum_all {sum_all}")
    print(f"sum_without_red {sum_without_red}")
