#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy

def parse_op_line(op):
    return re.match(r"^mem\[(\d+)\] = (\d+)$", op).groups()

def value_to_36_bit_char_list(v):
    return list(bin(int(v))[2:].zfill(36))

def part1(mask_groups):
    mem = defaultdict(lambda: 0)

    for mask, ops in mask_groups:
        for op in ops:
            address, value = parse_op_line(op)
            value_bin = value_to_36_bit_char_list(value)

            for idx, msk in enumerate(mask):
                if msk == '1':
                    value_bin[idx] = '1'
                if msk == '0':
                    value_bin[idx] = '0'

            mem[address] = int(''.join(value_bin), 2)

    return sum(mem.values())


def part2(mask_groups):
    mem = defaultdict(lambda: 0)

    for mask, ops in mask_groups:
        for op in ops:
            address, value = parse_op_line(op)
            address_bin = value_to_36_bit_char_list(address)
            value = int(value)

            x_count = 0
            for idx, msk in enumerate(mask):
                if msk == '1':
                    address_bin[idx] = '1'
                if msk == 'X':
                    address_bin[idx] = 'X'
                    x_count += 1

            address_pool = []
            for p in itertools.product(['0', '1'], repeat=x_count):
                next_address = address_bin.copy()
                xoc = 0
                for i, c in enumerate(next_address):
                    if c == 'X':
                        next_address[i] = p[xoc]
                        xoc += 1
                address_pool.append(int(''.join(next_address), 2))

            for adr in address_pool:
                mem[adr] = value

    return sum(mem.values())


with open('input') as f:
    mask_groups = f.read()[len('mask = '):].split('\nmask = ')
    mask_groups = list(map(lambda mg: (mg.splitlines()[0], mg.splitlines()[1:]), mask_groups))

    print(f"part1 {part1(mask_groups)}")
    print(f"part2 {part2(mask_groups)}")
