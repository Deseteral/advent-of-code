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

    # Part 1
    print(simulate_steps(64, level, (start_x, start_y)))

    # Part 2
    for i in range(3):
        step_count = start_x + (len(level) * i)
        print(simulate_steps(step_count, level, (start_x, start_y)))

        if __name__ == '__main__':
            main()
