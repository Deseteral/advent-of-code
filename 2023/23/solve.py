#!/usr/local/bin/python3
from collections import namedtuple

Point = namedtuple("Point", "x y")
Edge = namedtuple("Edge", "position distance")

neighbour_dir = [
    (0, -1),  # ^
    (0, 1),  # v
    (-1, 0),  # <
    (1, 0),  # >
]


def create_edges(level, with_slopes):
    edges = {}
    w = len(level[0])
    h = len(level)

    for y in range(h):
        for x in range(w):
            if level[y][x] == '#':
                continue

            nd = neighbour_dir
            if with_slopes and level[y][x] in '^v<>':
                nd = [neighbour_dir['^v<>'.index(level[y][x])]]

            neighbours = []
            for nx, ny in nd:
                dx = x + nx
                dy = y + ny

                if dx < 0 or dy < 0 or dx >= w or dy >= h:
                    continue
                if level[dy][dx] == '#':
                    continue
                neighbours.append(Edge(position=Point(dx, dy), distance=1))

            edges[Point(x, y)] = neighbours
    return edges


def optimize_edges(edges):
    nbr = {k: v for k, v in edges.items()}
    done = False
    while not done:
        done = True
        for current_node, current_node_edges in nbr.items():
            if len(current_node_edges) == 2:
                done = False

                a, b = current_node_edges

                an = nbr[a.position]
                atm = list(filter(lambda pp: pp.position == current_node, an))[0].distance
                an = list(filter(lambda pp: pp.position != current_node, an))
                an.append(Edge(position=b.position, distance=(atm + b.distance)))
                nbr[a.position] = an

                bn = nbr[b.position]
                btm = list(filter(lambda pp: pp[0] == current_node, bn))[0].distance
                bn = list(filter(lambda pp: pp[0] != current_node, bn))
                bn.append(Edge(position=a.position, distance=(btm + a.distance)))
                nbr[b.position] = bn

                del nbr[current_node]
                break
    return nbr


def find_max_distance(edges, start_point, end_point):
    queue = [(start_point, (), 0)]
    max_distance = 0

    while len(queue) > 0:
        position, visited, distance = queue.pop()

        if position == end_point:
            if distance > max_distance:
                max_distance = distance
            continue

        for neighbour_position, neighbour_distance in edges[position]:
            if neighbour_position not in visited:
                queue.append((neighbour_position, (*visited, position), (distance + neighbour_distance)))

    return max_distance


def main():
    file = open('input')
    lines = file.read().splitlines()

    level = [[x for x in line] for line in lines]
    w = len(level[0])
    h = len(level)

    edges_with_slopes = create_edges(level, with_slopes=True)
    edges_without_slopes = optimize_edges(create_edges(level, with_slopes=False))

    start_point = Point(1, 0)
    end_point = Point(w - 2, h - 1)

    print(find_max_distance(edges_with_slopes, start_point, end_point))
    print(find_max_distance(edges_without_slopes, start_point, end_point))


if __name__ == '__main__':
    main()
