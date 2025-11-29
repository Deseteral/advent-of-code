#!/usr/local/bin/python3
import math
from collections import defaultdict


def main():
    file = open('input')
    lines = file.read().splitlines()

    components = defaultdict(lambda: set())

    for line in lines:
        src, target = line.split(': ')
        target = target.split(' ')

        for t in target:
            components[src].add(t)
            components[t].add(src)

    # Used Graphviz to find two groups of components and three pairs of components connecting them.
    connections_to_cut = [('zsp', 'fhv'), ('fqr', 'bqp'), ('hcd', 'cnr')]

    src_queue = []
    for cs, ct in connections_to_cut:
        components[cs].remove(ct)
        components[ct].remove(cs)
        src_queue.append(cs)
        src_queue.append(ct)

    visited = set()
    group = -1
    group_size = []
    while len(src_queue) > 0:
        queue = [src_queue.pop()]
        group += 1
        group_size.append(0)

        while len(queue) > 0:
            curr = queue.pop()

            if curr in visited:
                continue

            visited.add(curr)
            group_size[group] += 1

            for n in components[curr]:
                queue.append(n)

    print(math.prod(filter(lambda x: x != 0, group_size)))


if __name__ == '__main__':
    main()
