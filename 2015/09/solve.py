#!/usr/local/bin/python3
import re
from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
        self.vertices = set()

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        self.vertices.add(from_node)
        self.vertices.add(to_node)

def get_min_results(results):
    return min(list(filter(lambda x: x >= 0 , results)))

def get_max_results(results):
    return max(list(filter(lambda x: x >= 0 , results)))

def traverse(source, target, dist, path, graph, is_minimalization):
    current_path = path.copy()

    dist += graph.weights[(source, target)]
    current_path.append(target)

    traversed = False
    results = []
    for e in graph.edges[target]:
        if not e in current_path:
            next_dist = traverse(target, e, dist, current_path, graph, is_minimalization)
            results.append(next_dist)
            traversed = True

    if not traversed and len(current_path) == len(graph.vertices): # done traversing
        return dist

    if not traversed and len(current_path) != len(graph.vertices): # dead end
        return -1

    if traversed:
        if is_minimalization:
            return get_min_results(results)
        else:
            return get_max_results(results)


with open('input') as f:
    lines = f.read().splitlines()

    graph = Graph()

    for line in lines:
        groups = re.match(r"^(.+) to (.+) = (\d+)$", line).groups()
        city_a, city_b, distance = groups
        distance = int(distance)

        graph.add_edge(*(city_a, city_b, distance))

    results_min = []
    results_max = []

    for v in graph.vertices:
        dist = 0
        path = [v]
        for e in graph.edges[v]:
            results_min.append(traverse(v, e, dist, path, graph, True))
            results_max.append(traverse(v, e, dist, path, graph, False))

    out_min = get_min_results(results_min)
    out_max = get_max_results(results_max)
    print(f"out_min {out_min}")
    print(f"out_max {out_max}")
