#!/usr/local/bin/python3
import re
import math
from collections import defaultdict

def calculate_distance_in_time(raindeer, time):
    cycle_time, distance, move_time = raindeer

    # distance after full cycles
    cycle_count = math.floor(time / cycle_time)
    distance_per_cycle = move_time * distance
    traveled = cycle_count * distance_per_cycle

    # add distance after the rest of time in not full cycle
    time_carried = time - (cycle_count * cycle_time)
    if time_carried > move_time:
        time_carried = move_time
    traveled += time_carried * distance

    return traveled

def calculate_max_distance_after_time(time):
    global raindeers

    max_distance = -1
    for r in raindeers.values():
        traveled = calculate_distance_in_time(r, time)
        max_distance = max(traveled, max_distance)

    return max_distance

def calculate_best_score_after_time(t):
    global raindeers

    leaderboard = defaultdict(lambda: (0, 0)) # (distance, points)

    for time in range(1, t+1):
        max_distance = -1

        # calculate distance for each raindeer
        for rk in raindeers.keys():
            traveled = calculate_distance_in_time(raindeers[rk], time)

            leaderboard[rk] = (traveled, leaderboard[rk][1])
            max_distance = max(traveled, max_distance)

        # assign points
        for rk in leaderboard.keys():
            if leaderboard[rk][0] == max_distance:
                leaderboard[rk] = (leaderboard[rk][0], leaderboard[rk][1] + 1)

    best_score = max(map(lambda x: x[1], leaderboard.values()))
    return best_score

raindeers = {}

with open('input') as f:
    lines = f.read().splitlines()

    for line in lines:
        name, speed, move_time, rest_time = re.match(r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$", line).groups()
        speed = int(speed)
        move_time = int(move_time)
        rest_time = int(rest_time)

        cycle_time = move_time + rest_time
        raindeers[name] = (cycle_time, speed, move_time)

    # part 1
    max_distance = calculate_max_distance_after_time(2503)
    print(f"max_distance: {max_distance}")

    # part 2
    best_score = calculate_best_score_after_time(2503)
    print(f"best_score: {best_score}")
