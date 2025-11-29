#!/usr/local/bin/python3
import sys
from collections import defaultdict


def main(input_file, _):
    lines = input_file.read().splitlines()

    connections = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        connections[a].add(b)
        connections[b].add(a)

    all_nodes = set(connections.keys())

    # Part 1
    sets_of_three = set()
    for t_node in filter(lambda n: n[0] == 't', all_nodes):
        for friend_of_t_node in connections[t_node]:
            for friend_of_friend in connections[friend_of_t_node]:
                if t_node in connections[friend_of_friend]:
                    s = frozenset([t_node, friend_of_t_node, friend_of_friend])
                    sets_of_three.add(s)

    print(len(sets_of_three))

    # Part 2
    def bron_kerbosch(r, p, x):
        if len(p) == 0 and len(x) == 0:
            return [r]

        results = []
        for v in list(p):
            results += bron_kerbosch({*r, v}, p & connections[v], x & connections[v])
            p -= {v}
            x = {*x, v}

        return results

    cliques = bron_kerbosch(set(), all_nodes, set())
    print(','.join(sorted(max(cliques, key=len))))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
