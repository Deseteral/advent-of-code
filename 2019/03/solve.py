#!/usr/local/bin/python3

def trace_wire_path(instructions):
    x, y = 0, 0
    step = 0

    for (direction, length) in instructions:
        for _ in range(0, length):
            step += 1

            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1

            yield ((x, y), step)

def main():
    file = open('input')
    lines = file.read().splitlines()

    wire1 = list(map(lambda x: (x[0], int(x[1:])), lines[0].split(',')))
    wire2 = list(map(lambda x: (x[0], int(x[1:])), lines[1].split(',')))

    # part 1
    wire1_tiles = set()
    wire2_tiles = set()

    for (pos, _) in trace_wire_path(wire1):
        wire1_tiles.add(pos)

    for (pos, _) in trace_wire_path(wire2):
        wire2_tiles.add(pos)

    crossings = list(wire1_tiles.intersection(wire2_tiles))

    min_distance = 99999
    for (cx, cy) in crossings:
        distance = abs(cx) + abs(cy)
        min_distance = min(min_distance, distance)

    print(min_distance)

    # part 2
    steps_to_crossing = [0] * len(crossings)

    for (pos, step) in trace_wire_path(wire1):
        if pos in crossings:
            idx = crossings.index(pos)
            steps_to_crossing[idx] += step

    for (pos, step) in trace_wire_path(wire2):
        if pos in crossings:
            idx = crossings.index(pos)
            steps_to_crossing[idx] += step

    print(min(steps_to_crossing))

if __name__ == '__main__': main()
