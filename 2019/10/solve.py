#!/usr/local/bin/python3
import math

def calc_angle(point, best_point):
    angle = math.atan2(
        (point[1] - best_point[1]) * -1,
        (point[0] - best_point[0]),
    )
    angle -= math.radians(90)
    angle = -angle
    if angle < 0: angle = angle + 2 * math.pi
    return abs(math.degrees(angle))

def reduce_coords(coords):
    a = coords[0]
    b = coords[1]
    gcd = -1

    while gcd != 1:
        gcd = math.gcd(a, b)
        a = int(a / gcd)
        b = int(b / gcd)

    return (a, b)

def main():
    file = open('input')
    lines = file.read().splitlines()


    asteroids = set()
    for y in range(len(lines)):
        for x in range(len(lines)):
            if (lines[y][x] == '#'): asteroids.add((x, y))

    # part 1
    best_detection_amount = -1
    best_coords = (0, 0)

    for coords in asteroids:
        relative = set()

        for a in asteroids:
            if coords == a: continue
            relative.add((a[0] - coords[0], a[1] - coords[1]))

        unique = set()
        for r in relative:
            unique.add(reduce_coords(r))

        if len(unique) > best_detection_amount:
            best_detection_amount = len(unique)
            best_coords = (coords[0], coords[1])

    print(best_detection_amount)

    # part 2
    to_be_destroyed = []

    for coords in asteroids:
        if coords == best_coords: continue
        angle = calc_angle(coords, best_coords)
        distance = abs(best_coords[0] - coords[0]) + abs(best_coords[1] - coords[1])
        to_be_destroyed.append((coords, angle, distance))

    angles = sorted(list(set(map(lambda e: e[1], to_be_destroyed))))

    destroy_count = 0
    while len(to_be_destroyed) > 0:
        for current_angle in angles:
            with_angle_by_distance = sorted(
                list(filter(lambda e: e[1] == current_angle, to_be_destroyed)),
                key=lambda e: e[2],
            )

            pick = with_angle_by_distance[0]

            to_be_destroyed.remove(pick)
            destroy_count += 1

            if destroy_count == 200:
                print(pick[0][0] * 100 + pick[0][1])
                return

if __name__ == '__main__': main()
