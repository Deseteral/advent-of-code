#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy

def rotate_point_around_origin(point, angle_deg):
    x, y = point
    rad = angle_deg * (math.pi / 180)
    nwx = round(x * math.cos(rad) - y * math.sin(rad))
    nwy = round(y * math.cos(rad) + x * math.sin(rad))

    return (nwx, nwy)

def manhattan_distance(x, y):
    return abs(x) + abs(y)

def simulate(starting_rot, commands):
    x = y = 0
    rot = starting_rot

    for ch, value in commands:
        if ch == 'N': y += value
        if ch == 'S': y -= value
        if ch == 'E': x += value
        if ch == 'W': x -= value
        if ch == 'R': rot = (rot + value) % 360
        if ch == 'L': rot = (rot - value) % 360
        if ch == 'F':
            if rot == 0: y += value
            if rot == 90: x += value
            if rot == 180: y -= value
            if rot == 270: x -= value

    return manhattan_distance(x, y)

def simulate_with_waypoint(starting_waypoint_pos, commands):
    x = y = 0
    wx, wy = starting_waypoint_pos

    for ch, value in commands:
        if ch == 'N':
            wy += value
        if ch == 'S':
            wy -= value
        if ch == 'E':
            wx += value
        if ch == 'W':
            wx -= value
        if ch == 'L':
            nwx, nwy = rotate_point_around_origin((wx, wy), value)
            wx = nwx
            wy = nwy
        if ch == 'R':
            nwx, nwy = rotate_point_around_origin((wx, wy), (360 - value))
            wx = nwx
            wy = nwy
        if ch == 'F':
            x += wx * value
            y += wy * value

    return manhattan_distance(x, y)

with open('input') as f:
    commands = [(line[0], int(line[1:])) for line in f.read().splitlines()]

    manhattan_distance_1 = simulate(90, commands)
    print(f"manhattan_distance_1 {manhattan_distance_1}")

    manhattan_distance_2 = simulate_with_waypoint((10, 1), commands)
    print(f"manhattan_distance_2 {manhattan_distance_2}")
