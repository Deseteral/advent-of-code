#!/usr/local/bin/python3

def get_priority(char):
    if (char.islower()):
        return ord(char) - 96
    else:
        return 27 + ord(char) - 65

def chunks(list, chunk_size):
    for i in range(0, len(list), chunk_size): yield list[i:i + chunk_size]

with open('input') as f:
    lines = f.read().splitlines()

    # part 1
    total_a = 0

    for line in lines:
        sp = int(len(line) / 2)
        first = line[:sp]
        second = line[sp:]

        for fl in first:
            if fl in second:
                total_a += get_priority(fl)
                break

    print(total_a)

    # part 2
    groups = list(chunks(lines, 3))
    total_b = 0

    for group in groups:
        common_el_set = set(group[0]).intersection(group[1]).intersection(group[2])
        common_el = list(common_el_set)[0]
        total_b += get_priority(common_el)

    print(total_b)
