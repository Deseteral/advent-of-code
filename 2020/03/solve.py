#!/usr/local/bin/python3

def traverse(right, down, lines):
    tree_count = 0
    x = 0
    y = 0

    width = len(lines[0])
    height = len(lines)

    while y < height:
        if lines[y][x % width] == '#':
            tree_count += 1

        y += down
        x += right

    return tree_count

with open('input') as f:
    lines = f.read().splitlines()

    # part 1
    result_first = traverse(3, 1, lines)
    print(f"result_first {result_first}")

    # part 2
    directions = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    result = list(map(lambda pos: traverse(*pos, lines), directions))

    result_multiplied = 1
    for num in result:
        result_multiplied *= num

    print(f"result_multiplied {result_multiplied}")

