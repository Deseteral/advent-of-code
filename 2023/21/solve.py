#!/usr/local/bin/python3


neighbour_dir = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def simulate_steps(step_count, level, start_pos):
    reached = set()
    reached.add(start_pos)

    map_size = len(level)

    for c in range(step_count):
        nr = set()
        while len(reached) > 0:
            x, y = reached.pop()
            for nx, ny in neighbour_dir:
                dx = (x + nx)
                dy = (y + ny)
                if level[dy % map_size][dx % map_size] == '.':
                    nr.add((dx, dy))
        reached = nr

    return len(reached)


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Find start
    start_x, start_y = None, None

    for y, line in enumerate(lines):
        if 'S' in line:
            start_y = y
            start_x = line.index('S')
            lines[y] = line.replace('S', '.')
            break

    level = [[x for x in line] for line in lines]
    level_size = len(level)

    # Part 1
    p1_result = simulate_steps(64, level, (start_x, start_y))
    print(f"result for 64 steps = {p1_result}")

    # Part 2
    for i in range(3):
        step_count = start_x + (level_size * i)
        print(f"x{i} = {simulate_steps(step_count, level, (start_x, start_y))}")

    target_steps = 26501365

    # Given x0, x1, x2 I have asked Wolfram Alpha to give me a second degree
    # polynomial that fits this values. The result is used below.
    x = (target_steps - start_x) // level_size
    result = (15286 * (x ** 2)) + (15394 * x) + 3884

    print(f"result for {target_steps} steps = {result}")


if __name__ == '__main__':
    main()
