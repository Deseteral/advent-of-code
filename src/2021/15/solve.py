#!/usr/local/bin/python3
from collections import defaultdict
import heapq

def grid_to_edge_list(grid):
    adj_points = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]

    edges = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for dx, dy in adj_points:
                tx = x + dx
                ty = y + dy

                if tx < 0: continue
                if tx >= len(grid[0]): continue
                if ty < 0: continue
                if ty >= len(grid): continue

                edges.append((f"{x}-{y}", f"{tx}-{ty}", grid[ty][tx]))
    return edges

def end_coordintate(grid):
    return f"{len(grid[0])-1}-{len(grid)-1}"

def dijkstra(edges, source, sink):
    graph = defaultdict(list)
    for l, r, c in edges: graph[l].append((c, r))
    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == sink: return (cost, path)
            for c, neighbour in graph[node]:
                if neighbour not in visited: heapq.heappush(queue, (cost+c, neighbour, path))
    return float("inf")

with open('input') as f:
    lines = f.read().splitlines()
    grid = [[int(x) for x in line] for line in lines]

    # starting grid
    edges = grid_to_edge_list(grid)
    cost, _ = dijkstra(edges, "0-0", end_coordintate(grid))
    print(f"cost {cost}")

    # larger grid
    org_y_len = len(grid)
    for repeat_count in range(1, 5):
        for y in range(org_y_len):
            new_row = [(grid[y][x] + repeat_count) if (grid[y][x] + repeat_count) <= 9 else ((grid[y][x] + repeat_count) - 9) for x in range(len(grid[y]))]
            grid.append(new_row)

    for y in range(len(grid)):
        org_len = len(grid[y])
        for repeat_count in range(1, 5):
            for x in range(org_len):
                next_value = (grid[y][x] + repeat_count) if (grid[y][x] + repeat_count) <= 9 else ((grid[y][x] + repeat_count) - 9)
                grid[y].append(next_value)


    larger_grid_edges = grid_to_edge_list(grid)
    larger_grid_cost, _ = dijkstra(larger_grid_edges, "0-0", end_coordintate(grid))
    print(f"larger_grid_cost {larger_grid_cost}")
