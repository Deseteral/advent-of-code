#!/usr/local/bin/python3
from collections import defaultdict
from copy import deepcopy


def main():
    file = open('input')
    lines = file.read().splitlines()

    comp = defaultdict(lambda: set())
    connections = set()

    for line in lines:
        src, target = line.split(': ')
        target = target.split(' ')

        for t in target:
            comp[src].add(t)
            comp[t].add(src)
            c = tuple(sorted([src, t]))
            connections.add(c)

    # for cut in itertools.combinations(connections, 3):
    for cut in [(('zsp', 'fhv'), ('fqr', 'bqp'), ('hcd', 'cnr'))]:
        cc = deepcopy(comp)
        src_queue = []
        for cs, ct in cut:
            cc[cs].remove(ct)
            cc[ct].remove(cs)
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

                for n in cc[curr]:
                    queue.append(n)

        if group_size[1] != 0:
            print(group_size[0] * group_size[1])


if __name__ == '__main__':
    main()
