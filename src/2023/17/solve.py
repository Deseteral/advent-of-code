#!/usr/local/bin/python3
from queue import PriorityQueue

neighbour_dir = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]


def dijkstra(starting_nodes, calc_edges_fn, calc_node_weight_fn, end_node_query_fn):
    best_distance = {}
    queue = PriorityQueue()

    for node in starting_nodes:
        queue.put((0, node))

    while not queue.empty():
        distance, node = queue.get()

        if node in best_distance:
            continue

        best_distance[node] = distance

        for neighbour_node in calc_edges_fn(node):
            if neighbour_node not in best_distance:
                next_dist = best_distance[node] + calc_node_weight_fn(neighbour_node)
                queue.put((next_dist, neighbour_node))

    end_nodes = []
    for node, distance in best_distance.items():
        if end_node_query_fn(node):
            end_nodes.append((distance, node))

    return end_nodes, best_distance


def main():
    file = open('input')
    lines = file.read().splitlines()

    level = [[int(c) for c in line] for line in lines]
    w = len(lines[0])
    h = len(lines)

    starting_nodes = [
        ((0, 0), (1, 0), 0),
        ((0, 0), (0, 1), 0),
    ]

    def calc_node_weight(node):
        (x, y), _, _ = node
        return level[y][x]

    def calc_edges_fn(is_part_1):
        def inner(current_node):
            (x, y), direction, same_dir_length = current_node

            next_nodes = []

            for nn in neighbour_dir:
                nx, ny = nn
                xx = x + nx
                yy = y + ny

                if xx < 0 or yy < 0 or xx >= w or yy >= h:
                    continue

                is_reverse_dir = (direction[0] == -nx) and (direction[1] == -ny)
                if is_reverse_dir:
                    continue

                is_same_dir = (nn == direction)

                if is_part_1:
                    if is_same_dir and ((same_dir_length + 1) > 3):
                        continue
                else:
                    if is_same_dir and ((same_dir_length + 1) > 10):
                        continue
                    if not is_same_dir and (same_dir_length < 4):
                        continue

                next_node = ((xx, yy), (nx, ny), 1 if nn != direction else (same_dir_length + 1))
                next_nodes.append(next_node)
            return next_nodes

        return inner

    def end_node_query_part1(node):
        (x, y), _, same_dir_length = node
        return (x == (w - 1)) and (y == (h - 1))

    def end_node_query_part2(node):
        (x, y), _, same_dir_length = node
        return (x == (w - 1)) and (y == (h - 1)) and (same_dir_length >= 4)

    end_nodes, _ = dijkstra(starting_nodes, calc_edges_fn(is_part_1=True), calc_node_weight, end_node_query_part1)
    print(end_nodes[0][0])

    end_nodes, _ = dijkstra(starting_nodes, calc_edges_fn(is_part_1=False), calc_node_weight, end_node_query_part2)
    print(end_nodes[0][0])


if __name__ == '__main__':
    main()
