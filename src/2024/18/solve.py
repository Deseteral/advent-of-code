#!/usr/local/bin/python3
import sys
from queue import PriorityQueue


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def scale(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Vec2({self.x} {self.y})"

    def __repr__(self):
        return f"Vec2({self.x} {self.y})"

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")

    def copy(self):
        return Vec2(self.x, self.y)

    def distance(self, to):
        return Vec2(to.x - self.x, to.y - self.y)

    def __lt__(self, other):
        return False


directions = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0),
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


def main(input_file, env_test_run):
    lines = input_file.read().splitlines()

    w = 70 + 1 if not env_test_run else 6 + 1
    h = 70 + 1 if not env_test_run else 6 + 1

    start_pos = Vec2(0, 0)
    end_pos = Vec2(70, 70) if not env_test_run else Vec2(6, 6)
    steps_to_simulate = 1024 if not env_test_run else 12

    level = [['.' for _ in range(w)] for _ in range(h)]

    def set_at_pos(value, pos):
        if pos.x < 0 or pos.y < 0 or pos.x >= w or pos.y >= h:
            return
        level[pos.y][pos.x] = value

    def at_pos(pos):
        if pos.x < 0 or pos.y < 0 or pos.x >= w or pos.y >= h:
            return None
        return level[pos.y][pos.x]

    for line in lines[:steps_to_simulate]:
        x, y = map(int, line.split(','))
        set_at_pos('#', Vec2(x, y))

    def calc_edges_fn(current_node_pos):
        next_nodes = []
        for nn in directions:
            np = current_node_pos + nn
            if at_pos(np) == '.':
                next_nodes.append(np)
        return next_nodes

    def calc_node_weight(_):
        return 1

    def end_node_query_fn(current_node_pos):
        return current_node_pos == end_pos

    # Part 1
    _, best_distance = dijkstra([start_pos], calc_edges_fn, calc_node_weight, end_node_query_fn)
    print(best_distance[end_pos])

    # Part 2
    for line in lines[steps_to_simulate:]:
        x, y = map(int, line.split(','))
        set_at_pos('#', Vec2(x, y))

        _, best_distance = dijkstra([start_pos], calc_edges_fn, calc_node_weight, end_node_query_fn)
        if not end_pos in best_distance:
            print(line)
            break


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
