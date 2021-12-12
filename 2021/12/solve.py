#!/usr/local/bin/python3
from collections import defaultdict

def cave_is_big(cave): return cave.isupper()
def occurences(element, arr): return len(list(filter(lambda x: x == element, arr)))
def count_valid_paths(paths): return len(list(filter( lambda path: path[-1] == 'end', paths)))

simple_traversal_visited_list = []
def simple_traversal(graph, current_vertex, visited):
    visited.append(current_vertex)

    for vertex in graph[current_vertex]:
        if vertex not in visited or cave_is_big(vertex):
            simple_traversal(graph, vertex, visited.copy())

    simple_traversal_visited_list.append(visited)

traversal_visited_list = []
def traversal(graph, current_vertex, visited, visited_small_twice):
    if current_vertex in ['start', 'end'] and current_vertex in visited: return

    visited.append(current_vertex)

    for vertex in graph[current_vertex]:
        if cave_is_big(vertex):
            traversal(graph, vertex, visited.copy(), visited_small_twice)
        else:
            if visited_small_twice:
                if occurences(vertex, visited) == 0:
                    traversal(graph, vertex, visited.copy(), visited_small_twice)
            else:
                will_visit_twice = occurences(vertex, visited) == 1
                traversal(graph, vertex, visited.copy(), will_visit_twice)

    traversal_visited_list.append(visited)

with open('input') as f:
    lines = f.read().splitlines()

    # parse input and build graph
    graph = defaultdict(lambda: [])

    for line in lines:
        source, destination = line.split('-')
        graph[source].append(destination)
        graph[destination].append(source)

    # part 1
    simple_traversal(graph, 'start', [])
    simple_traversal_path_count = count_valid_paths(simple_traversal_visited_list)
    print(f"simple_traversal_path_count {simple_traversal_path_count}")

    # part 2
    traversal(graph, 'start', [], False)
    traversal_path_count = count_valid_paths(traversal_visited_list)
    print(f"traversal_path_count {traversal_path_count}")
