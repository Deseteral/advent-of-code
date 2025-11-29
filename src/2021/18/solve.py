#!/usr/local/bin/python3
import math
import itertools
from copy import deepcopy

LEFT = 1
RIGHT = 2

class Value:
    def __init__(self, value, parent, side):
        self.value = value
        self.parent = parent
        self.side = side

class Pair:
    def __init__(self, parent, side):
        self.left = None
        self.right = None
        self.parent = parent
        self.side = side

def reverse_dir(dir):
    return RIGHT if dir == LEFT else LEFT

def get_level(node):
    prev = node
    level = 0
    while prev != None:
        level += 1
        prev = prev.parent
    return level

def get_magnitude(node):
    if type(node) is Value: return node.value
    return (get_magnitude(node.left) * 3) + (get_magnitude(node.right) * 2)

def find_dir_most(node, dir):
    prev = node
    while type(prev) is Pair: prev = prev.left if dir == LEFT else prev.right
    return prev

def find_neighbour_of(node, dir):
    current = node
    parent = node.parent

    while True:
        if (dir == LEFT and parent.left == current) or (dir == RIGHT and parent.right == current):
            current = parent
            parent = parent.parent
            if parent == None:
                return None
        else:
            return find_dir_most(parent.left if dir == LEFT else parent.right, reverse_dir(dir))

def explode(node):
    target_node = find_dir_most(node, LEFT)

    while target_node != None:
        if get_level(target_node) > 5: break
        target_node = find_neighbour_of(target_node, RIGHT)

    if target_node == None:
        return False

    target_node = target_node.parent

    left_neighbour = find_neighbour_of(target_node, LEFT)
    if left_neighbour != None:
        left_neighbour.value += target_node.left.value

    right_neighbour = find_neighbour_of(target_node, RIGHT)
    if right_neighbour != None:
        right_neighbour.value += target_node.right.value

    if target_node.side == LEFT:
        target_node.parent.left = Value(0, target_node.parent, LEFT)
    else:
        target_node.parent.right = Value(0, target_node.parent, RIGHT)

    return True

def split_node(node):
    p = Pair(node.parent, node.side)
    p.left = Value(math.floor(node.value / 2), p, LEFT)
    p.right = Value(math.ceil(node.value / 2), p, RIGHT)

    if node.side == LEFT:
        node.parent.left = p
    else:
        node.parent.right = p

def reduce_node(node):
    while True:
        did_explode = True
        while did_explode:
            did_explode = explode(node)

        to_be_split = find_dir_most(node, LEFT)
        while to_be_split != None:
            if to_be_split.value >= 10:
                split_node(to_be_split)
                break
            else:
                to_be_split = find_neighbour_of(to_be_split, RIGHT)

        if to_be_split == None:
            break

def node_from_array(arr, parent, side):
    if type(arr) is int: return Value(arr, parent, side)

    p = Pair(parent, side)
    p.left = node_from_array(arr[0], p, LEFT)
    p.right = node_from_array(arr[1], p, RIGHT)
    return p

def add_nodes(node_a, node_b):
    acc = Pair(None, None)

    acc.left = node_a
    acc.left.parent = acc
    acc.left.side = LEFT

    acc.right = node_b
    acc.right.parent = acc
    acc.right.side = RIGHT

    reduce_node(acc)
    return acc

with open('input') as f:
    lines = f.read().splitlines()

    lines = list(map(lambda arr_str: node_from_array(eval(arr_str), None, None), lines))

    # part 1
    acc = lines[0]
    addition_list = deepcopy(lines)
    for line in addition_list[1:]:
        acc = add_nodes(acc, line)

    magnitude = get_magnitude(acc)
    print(magnitude)

    # part 2
    max_magnitude = -1
    for permutation in itertools.permutations(lines, 2):
        a = deepcopy(permutation[0])
        b = deepcopy(permutation[1])
        current_magnitude = get_magnitude(add_nodes(a, b))
        if current_magnitude > max_magnitude:
            max_magnitude = current_magnitude

    print(max_magnitude)
