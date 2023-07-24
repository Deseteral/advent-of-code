#!/usr/local/bin/python3
import re
import math
import itertools

def calc_energy(moon):
    potential = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
    kinetic = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
    return potential * kinetic

def main():
    file = open('input')
    lines = file.read().splitlines()

    moons = []

    for line in lines:
        groups = re.match(r"^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$", line).groups()
        moons.append((
            [int(groups[0]), int(groups[1]), int(groups[2])],
            [0, 0, 0],
        ))

    total_energy = -1

    axis_hashes = [set(), set(), set()]
    repetition_idx = [None, None, None]

    for time_step in itertools.count():
        # apply gravity
        for (moon_a, moon_b) in itertools.combinations(moons, 2):
            pos_a = moon_a[0]
            vel_a = moon_a[1]
            pos_b = moon_b[0]
            vel_b = moon_b[1]

            for dimension in range(0, 3):
                if pos_a[dimension] > pos_b[dimension]:
                    vel_a[dimension] -= 1
                    vel_b[dimension] += 1
                elif pos_a[dimension] < pos_b[dimension]:
                    vel_a[dimension] += 1
                    vel_b[dimension] -= 1

        # apply velocity
        for moon in moons:
            for dimension in range(0, 3):
                moon[0][dimension] += moon[1][dimension]

        if time_step == 1000:
            total_energy = sum(map(calc_energy, moons))

        for dimension in range(0, 3):
            if repetition_idx[dimension] is not None:
                continue

            axis_hash = str([(moon[0][dimension], moon[1][dimension]) for moon in moons])

            if axis_hash in axis_hashes[dimension]:
                repetition_idx[dimension] = time_step
            else:
                axis_hashes[dimension].add(axis_hash)

        if None not in repetition_idx:
            break

    print(total_energy)
    print(math.lcm(*repetition_idx))

if __name__ == '__main__': main()
