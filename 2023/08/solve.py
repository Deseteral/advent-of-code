#!/usr/local/bin/python3
import math


def main():
    file = open('input')
    lines = file.read().splitlines()

    movement = lines[0]
    tree = dict()

    for line in lines[2:]:
        src, dst = line.split(' = ')
        l, r = dst.split(', ')
        tree[src] = (l[1:], r[:-1])

    position = 'AAA'
    steps_needed = -1
    ghosts_positions = list(filter(lambda m: m[2] == 'A', tree.keys()))
    ghosts_steps_needed = [-1 for _ in range(len(ghosts_positions))]
    movement_idx = 0
    step = 0
    done = False
    while not done:
        current_movement_idx = 0 if movement[movement_idx] == 'L' else 1

        position = tree[position][current_movement_idx]

        for pidx, p in enumerate(ghosts_positions):
            ghosts_positions[pidx] = tree[p][current_movement_idx]

        step += 1
        movement_idx = (movement_idx + 1) % len(movement)

        if position == 'ZZZ' and steps_needed == -1:
            steps_needed = step

        for pidx, p in enumerate(ghosts_positions):
            if p[2] == 'Z' and ghosts_steps_needed[pidx] == -1:
                ghosts_steps_needed[pidx] = step

        done = steps_needed != -1 and all(s != -1 for s in ghosts_steps_needed)

    print(steps_needed)
    print(math.lcm(*ghosts_steps_needed))


if __name__ == '__main__':
    main()
