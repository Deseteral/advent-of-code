#!/usr/local/bin/python3
import re
from collections import defaultdict

def get_count_1(bag_type, searching_for):
    global sources
    bag_defs = sources[bag_type]

    if bag_defs == None:
        return 0

    count = 0
    for d in bag_defs:
        if d[0] == searching_for:
            count += 1
        else:
            count += get_count_1(d[0], searching_for)

    return count

def get_count_2(root_bag_type):
    global sources
    bag_defs = sources[root_bag_type]

    if bag_defs == None:
        return 1

    count = 1
    for definition in bag_defs:
        bag_type, amount = definition
        count += (amount * get_count_2(bag_type))

    return count


sources = defaultdict(list)

with open('input') as f:
    lines = f.read().splitlines()

    for line in lines:
        outer, inner = re.match(r"^(.+) bags contain (.+)\.$", line).groups()

        if 'no other bag' in inner:
            sources[outer] = None
        else:
            for b in inner.split(', '):
                amount, bag_type = re.match(r"^(\d+) (.+) bags?$", b).groups()
                amount = int(amount)
                sources[outer].append((bag_type, amount))


    # part 1
    successful_paths = 0
    for key in sources.keys():
        if get_count_1(key, 'shiny gold') > 0:
            successful_paths += 1
    print(successful_paths)

    # part 2
    ans2 = (get_count_2('shiny gold') - 1)
    print(ans2)
