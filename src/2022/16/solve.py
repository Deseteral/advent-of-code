#!/usr/local/bin/python3
import re
from copy import deepcopy
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight=1):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    d = {v: float('inf') for v in range(graph.v)}
    d[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = d[neighbor]
                    new_cost = d[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        d[neighbor] = new_cost
    return d

best_value = -1
best_value_with_elephant = -1

def traverse(open_valves, total_value, current_pos, time_left):
    global best_value

    best_value = max(total_value, best_value)

    if time_left <= 0:
        return

    if current_pos in open_valves:
        d = navigation[current_pos]
        for left_to_open in (active_valves - open_valves):
            cost = d[id_to_idx[left_to_open]]
            traverse(open_valves, total_value, left_to_open, time_left - cost)
    else:
        valve_id = id_to_idx[current_pos]
        rate = valves[valve_id][1]
        value = time_left * rate

        next_visited = open_valves | set([current_pos])
        next_total_value = total_value + value

        traverse(next_visited, next_total_value, current_pos, time_left - 1)


def traverse_with_elephant(open_valves, total_value, current_pos, time_left, is_player_turn):
    global best_value_with_elephant

    best_value_with_elephant = max(total_value, best_value_with_elephant)

    if time_left <= 0:
        return

    if current_pos in open_valves:
        d = navigation[current_pos]
        for left_to_open in (active_valves - open_valves):
            destination = id_to_idx[left_to_open]
            cost = d[destination]
            traverse_with_elephant(open_valves, total_value, left_to_open, time_left - cost, is_player_turn)
    else:
        valve_id = id_to_idx[current_pos]
        rate = valves[valve_id][1]
        value = time_left * rate

        next_visited = open_valves | set([current_pos])
        next_total_value = total_value + value

        traverse_with_elephant(next_visited, next_total_value, current_pos, time_left - 1, is_player_turn)

        if is_player_turn:
            traverse_with_elephant(next_visited, next_total_value, 'AA', 26-1, False)

with open('input') as f:
    lines = f.read().splitlines()

    # parsing
    id_to_idx = dict()
    valves = []
    active_valves = set()

    for idx, line in enumerate(lines):
        valve, rate, leads = re.match(r"^Valve (.{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$", line).groups()
        rate = int(rate)
        leads = leads.split(', ')

        id_to_idx[valve] = idx
        valves.append((valve, rate, leads))

        if rate > 0:
            active_valves.add(valve)

    # creating graph
    g = Graph(len(valves))

    for valve_from, _, leads in valves:
        for valve_to in leads:
            g.add_edge(id_to_idx[valve_from], id_to_idx[valve_to])

    # precalculating all possible routes
    navigation = dict()
    for valve in (active_valves | set(['AA'])):
        navigation[valve] = dijkstra(deepcopy(g), id_to_idx[valve])

    # part 1
    traverse(set(['AA']), 0, 'AA', 30-1)
    print(best_value)

    # part 2
    traverse_with_elephant(set(['AA']), 0, 'AA', 26-1, True)
    print(best_value_with_elephant)
