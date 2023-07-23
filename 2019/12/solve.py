#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy
import numpy as np

# def add_vectors(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])

def calc_energy(moon):
    potential = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
    kinetic = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
    return potential * kinetic

def main():
    file = open('input')
    # file = open('test_input')
    lines = file.read().splitlines()

    moons = []

    for line in lines:
        groups = re.match(r"^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$", line).groups()
        moons.append((
            [int(groups[0]), int(groups[1]), int(groups[2])],
            [0, 0, 0],
        ))

    for _time_step in range(1000):
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

    for moon in moons:
        potential = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
        kinetic = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
        energy = potential * kinetic

    total_energy = sum(map(calc_energy, moons))
    print(total_energy)

if __name__ == '__main__': main()
