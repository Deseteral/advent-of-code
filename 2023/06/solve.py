#!/usr/local/bin/python3
import math


def go_race(race_params):
    possibilites = []
    for race_idx in range(0, len(race_params[0])):
        max_time = race_params[0][race_idx]
        distance_to_beat = race_params[1][race_idx]

        possibility_count = 0
        for hold_time in range(1, max_time):
            move_time = max_time - hold_time
            distance = hold_time * move_time
            if distance > distance_to_beat:
                possibility_count += 1
        possibilites.append(possibility_count)

    return math.prod(possibilites)


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Part 1
    race_params = [list(map(int, filter(len, line.split(':')[1].split(' ')))) for line in lines]
    print(go_race(race_params))

    # Part 2
    race_params = [[int(line.split(':')[1].replace(' ', ''))] for line in lines]
    print(go_race(race_params))


if __name__ == '__main__':
    main()
