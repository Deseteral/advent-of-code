#!/usr/local/bin/python3
import itertools

neighbour_dir = [
    (1, 0),  # R
    (0, 1),  # D
    (-1, 0),  # L
    (0, -1),  # U
]


def shoelace(points):
    area = 0
    for (x, y), (xx, yy) in itertools.pairwise(points):
        area += ((x * yy) - (xx * y))
    return area // 2


def picks(area, perimeter):
    return area + int(perimeter / 2) - 1


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Part 1
    vertices = []
    perimeter = 0
    x, y = (0, 0)
    for line in lines:
        direction, amount, _ = line.split(' ')
        amount = int(amount)
        dir_idx = 'RDLU'.index(direction)

        dx, dy = neighbour_dir[dir_idx]
        x += (dx * amount)
        y += (dy * amount)
        perimeter += amount
        vertices.append((x, y))

    tile_count = picks(shoelace(vertices), perimeter) + 2
    print(tile_count)

    # Part 2
    vertices = []
    perimeter = 0
    x, y = (0, 0)
    for line in lines:
        _, _, color = line.split(' ')
        color = color[2:-1]
        amount = int(color[:5], 16)
        dir_idx = int(color[-1])

        dx, dy = neighbour_dir[dir_idx]
        x += (dx * amount)
        y += (dy * amount)
        perimeter += amount
        vertices.append((x, y))

    tile_count = picks(shoelace(vertices), perimeter) + 2
    print(tile_count)


if __name__ == '__main__':
    main()
