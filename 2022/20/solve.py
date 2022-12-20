#!/usr/local/bin/python3
from copy import deepcopy

class Node:
    def __init__(self, v):
        self.value = v

def do_the_mixing(nodes):
    for node in nodes:
        jumps = node.value % (len(nodes)-1)

        if jumps == 0:
            continue

        selector = node
        for _ in range(jumps):
            selector = selector.next

        current_prev = node.prev
        current_next = node.next
        current_s_next = selector.next

        selector.next = node
        node.prev = selector

        node.next = current_s_next
        current_s_next.prev = node

        current_prev.next = current_next
        current_next.prev = current_prev

def calc_coord_sum(nodes):
    zero_node = None
    for node in nodes:
        if node.value == 0:
            zero_node = node
            break

    coord_sum = 0
    selector = zero_node
    for jump in range(1, 3000+1):
        selector = selector.next
        if jump % 1000 == 0: coord_sum += selector.value
    return coord_sum

def as_linked_list(nodes):
    for idx, node in enumerate(nodes):
        node.next = nodes[(idx+1) % len(nodes)]
        node.prev = nodes[idx-1]

with open('input') as f:
    lines = f.read().splitlines()

    # parsing
    nodes = []
    for line in lines:
        nodes.append(Node(int(line)))

    # part 1
    encrypted_nodes = deepcopy(nodes)
    as_linked_list(encrypted_nodes)
    do_the_mixing(encrypted_nodes)
    print(calc_coord_sum(encrypted_nodes))

    # part 2
    decrypted_nodes = deepcopy(nodes)
    as_linked_list(decrypted_nodes)
    for node in decrypted_nodes:
        node.value *= 811589153

    for _ in range(10):
        do_the_mixing(decrypted_nodes)

    print(calc_coord_sum(decrypted_nodes))
