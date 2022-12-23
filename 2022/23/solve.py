#!/usr/local/bin/python3
from collections import defaultdict
from copy import deepcopy
import sys

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)
NW = (-1, -1)
NE = (1, -1)
SE = (1, 1)
SW = (-1, 1)

neighbour_dir = [
    NW,
    N,
    NE,
    W,
    E,
    SW,
    S,
    SE,
]

def check_neighbours(elf_pos, nlist, l):
    count = 0
    for nd in nlist:
        if (elf_pos[0] + nd[0], elf_pos[1] + nd[1]) in l:
            count += 1
    return count

def simulate_round(level, consider_dir):
    proposed_moves = defaultdict(lambda: None)
    did_move = False

    # first half of the round
    for elf_idx, elf_pos in enumerate(level):
        if check_neighbours(elf_pos, neighbour_dir, level) == 0:
            continue

        for looking_directions, target_dir in consider_dir:
            if check_neighbours(elf_pos, looking_directions, level) == 0:
                proposed_moves[elf_idx] = (elf_pos[0] + target_dir[0], elf_pos[1] + target_dir[1])
                break

    # second half of the round
    next_level = []
    for elf_idx, elf_pos in enumerate(level):
        proposed_move = proposed_moves[elf_idx]

        if proposed_move == None:
            next_level.append(elf_pos)
            continue

        is_move_duplicated = False
        for other_elf_idx, other_elf_move in proposed_moves.items():
            if other_elf_idx == elf_idx: continue
            if proposed_move == other_elf_move:
                is_move_duplicated = True
                break

        if not is_move_duplicated:
            next_level.append(proposed_move)
            did_move = True
        else:
            next_level.append(elf_pos)

    consider_dir.append(consider_dir.pop(0))

    return (next_level, did_move)

def main():
    with open('input') as f:
        lines = f.read().splitlines()

        # parsing
        elf_positions = []

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    elf_positions.append((x,y))

        # part 1
        level_1 = deepcopy(elf_positions)
        consider_dir = [
            ([N, NE, NW], N),
            ([S, SE, SW], S),
            ([W, NW, SW], W),
            ([E, NE, SE], E),
        ]

        for _ in range(10):
            next_level, _ = simulate_round(level_1, consider_dir)
            level_1 = next_level

        x_pos = list(map(lambda elf: elf[0], level_1))
        y_pos = list(map(lambda elf: elf[1], level_1))
        bounds = (
            (min(x_pos), max(x_pos)),
            (min(y_pos), max(y_pos)),
        )

        area = (bounds[0][1] + 1 - bounds[0][0]) * (bounds[1][1] + 1 - bounds[1][0])
        print(area - len(level_1))

        # part 2
        level_2 = deepcopy(elf_positions)
        consider_dir = [
            ([N, NE, NW], N),
            ([S, SE, SW], S),
            ([W, NW, SW], W),
            ([E, NE, SE], E),
        ]

        for round_idx in range(1, sys.maxsize):
            next_level, did_move = simulate_round(level_2, consider_dir)

            level_2 = next_level

            if did_move == False:
                print(round_idx)
                break

if __name__ == '__main__': main()
