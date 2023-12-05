#!/usr/local/bin/python3
import math

categories = []


def map_value_to_next_category(value, category):
    for dst_start, src_range, _ in category:
        if value in src_range:
            offset = value - src_range[0]
            return dst_start + offset
    return value


def map_seed_to_location(initial_value):
    value = initial_value
    for cat in categories:
        value = map_value_to_next_category(value, cat)
    return value


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Parsing
    seeds = [int(x) for x in lines[0].split(': ')[1].split(' ')]

    current_category = []
    for line in list(filter(len, lines[3:])):
        if line[0].isdigit():
            dst_start, src_start, map_len = [int(x) for x in line.split(' ')]
            src_range = range(src_start, src_start + map_len)
            current_category.append((dst_start, src_range, map_len))
        else:
            categories.append(current_category)
            current_category = []
    categories.append(current_category)

    # Part 1
    print(min(map(map_seed_to_location, seeds)))

    # Part 2
    approx_min = math.inf
    approx_range = None
    for seed_idx in range(0, len(seeds), 2):
        rstart = seeds[seed_idx]
        rlen = seeds[seed_idx + 1]
        jmp = math.floor(math.sqrt(rlen))

        for seed in range(rstart, rstart + rlen, jmp):
            val = map_seed_to_location(seed)
            if val < approx_min:
                approx_min = val
                approx_range = range(seed - jmp, seed)

    accurate_min = math.inf
    for seed in approx_range:
        val = map_seed_to_location(seed)
        if val < accurate_min:
            accurate_min = val
    print(accurate_min)


if __name__ == '__main__':
    main()
