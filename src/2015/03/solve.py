#!/usr/local/bin/python3

def traverse(positions, instructions):
    visited = [(0,0)]

    for i in range(len(instructions)):
        mc = s[i]

        pos = positions[i % len(positions)]
        if mc == '<':
            pos[0] -= 1
        elif mc == '>':
            pos[0] += 1
        elif mc == '^':
            pos[1] += 1
        elif mc == 'v':
            pos[1] -= 1

        visited.append((pos[0], pos[1]))

    return len(list(dict.fromkeys(visited)))

with open('input') as f:
    s = f.read()

    positions1 = [
        [0, 0],
    ]
    positions2 = [
        [0, 0],
        [0, 0],
    ]

    unique_locations1 = traverse(positions1, s)
    unique_locations2 = traverse(positions2, s)

    print(f"unique_locations1 {unique_locations1}")
    print(f"unique_locations2 {unique_locations2}")
