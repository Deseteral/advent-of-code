#!/usr/local/bin/python3

neighbour_dir = [
    (0, 0, -1),
    (0, 0, +1),
    (0, -1, 0),
    (0, +1, 0),
    (-1, 0, 0),
    (+1, 0, 0),
]

with open('input') as f:
    lines = f.read().splitlines()

    cubes = set()
    for line in lines:
        cubes.add(tuple(map(int, line.split(','))))

    def values_in_axis(axis):
        return set(map(lambda c: c[axis], cubes))

    # part 1
    sides = 0
    for cc in cubes:
        for dc in neighbour_dir:
            lc = (cc[0] + dc[0], cc[1] + dc[1], cc[2] + dc[2])
            if lc not in cubes:
                sides += 1

    print(sides)

    # part 2
    sides = 0
    boundaries = [(min(values_in_axis(axis))-1, max(values_in_axis(axis))+1) for axis in (0, 1, 2)]

    visited = set()
    queue = [(boundaries[0][0], boundaries[1][0], boundaries[2][0])]

    while len(queue) > 0:
        cc = queue.pop(0)
        visited.add(cc)

        for dc in neighbour_dir:
            lc = (cc[0] + dc[0], cc[1] + dc[1], cc[2] + dc[2])

            if lc[0] < boundaries[0][0] or lc[0] > boundaries[0][1]: continue
            if lc[1] < boundaries[1][0] or lc[1] > boundaries[1][1]: continue
            if lc[2] < boundaries[2][0] or lc[2] > boundaries[2][1]: continue

            if lc in cubes:
                sides += 1
            elif lc not in visited and lc not in queue:
                queue.append(lc)

    print(sides)
