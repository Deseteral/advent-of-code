#!/usr/local/bin/python3
from collections import defaultdict
from operator import itemgetter


def lens_hash(ss):
    cv = 0
    for c in ss:
        cv += ord(c)
        cv *= 17
        cv %= 256
    return cv


def main():
    file = open('input')
    seq = file.read().splitlines()[0].split(',')

    # Part 1
    print(sum(map(lens_hash, seq)))

    # Part 2
    hm = defaultdict(lambda: [])

    for operation in seq:
        if '-' in operation:
            label = operation[:-1]
            label_hash = lens_hash(label)
            hash_map_labels = list(map(itemgetter(0), hm[label_hash]))
            if label in hash_map_labels:
                idx = hash_map_labels.index(label)
                hm[label_hash].pop(idx)

        if '=' in operation:
            label, value = operation.split('=')
            value = int(value)
            label_hash = lens_hash(label)
            hash_map_labels = list(map(itemgetter(0), hm[label_hash]))
            if label in hash_map_labels:
                idx = hash_map_labels.index(label)
                hm[label_hash][idx] = (label, value)
            else:
                hm[label_hash].append((label, value))

    total_focusing_power = 0
    for box_idx in range(256):
        for lens_idx, lens in enumerate(hm[box_idx]):
            total_focusing_power += (box_idx + 1) * (lens_idx + 1) * (lens[1])

    print(total_focusing_power)


if __name__ == '__main__':
    main()
