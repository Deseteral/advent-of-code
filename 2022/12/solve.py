#!/usr/local/bin/python3
from queue import PriorityQueue

neighbour_dir = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        # self.edges[v][u] = weight

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


with open('input') as f:
    lines = f.read().splitlines()

    starting_point = None
    finish_point = None

    lowest_points = []

    w = len(lines[0])
    h = len(lines)
    vertices = []

    # parsing
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            elevation = None
            idx = len(vertices)
            if c == 'S':
                elevation = 0
                starting_point = idx
            elif c == 'E':
                elevation = ord('z') - 97
                finish_point = idx
            else:
                elevation = ord(c) - 97

            if elevation == 0:
                lowest_points.append(idx)

            vertices.append(elevation)

    # creating graph
    graph = Graph(len(vertices))
    reverse_graph = Graph(len(vertices))

    for idx, elevation in enumerate(vertices):
        y = int(idx / w)
        x = int(idx % w)
        for nd in neighbour_dir:
            nx = x + nd[0]
            ny = y + nd[1]
            if nx < 0 or ny < 0 or nx >= w or ny >= h: continue

            nidx = nx + (ny * w)
            ne = vertices[nidx]

            if (elevation + 1) >= ne:
                graph.add_edge(idx, nidx, 1)
                reverse_graph.add_edge(nidx, idx, 1)

    # part 1
    print(dijkstra(graph, starting_point)[finish_point])

    # part 2
    best_length = 99999999
    rd = dijkstra(reverse_graph, finish_point)
    for p in lowest_points:
        length = rd[p]
        if length < best_length: best_length = length
    print(best_length)
