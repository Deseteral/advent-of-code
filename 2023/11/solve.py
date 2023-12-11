#!/usr/local/bin/python3
import itertools


def row_count(arr):
    return len(arr)


def col_count(arr):
    return len(arr[0])


def sum_distances(arr, exp_rate):
    # Expansion
    rows_to_expand = []
    for row_idx in range(row_count(arr)):
        if '#' not in arr[row_idx]:
            rows_to_expand.append(row_idx)

    columns_to_expand = []
    for col_idx in range(col_count(arr)):
        if '#' not in list(zip(*arr))[col_idx]:
            columns_to_expand.append(col_idx)

    # Count galaxies
    galaxies = []
    for ri, row in enumerate(arr):
        for ci, col in enumerate(row):
            if arr[ri][ci] == '#':
                galaxies.append((ri, ci))

    dist_sum = 0
    for fg, tg in list(itertools.combinations(range(len(galaxies)), 2)):
        fx, fy = galaxies[fg]
        tx, ty = galaxies[tg]

        bfx = len(list(filter(lambda q: q < fx, rows_to_expand)))
        fx = fx + (bfx * exp_rate)

        bfy = len(list(filter(lambda q: q < fy, columns_to_expand)))
        fy = fy + (bfy * exp_rate)

        btx = len(list(filter(lambda q: q < tx, rows_to_expand)))
        tx = tx + (btx * exp_rate)

        bty = len(list(filter(lambda q: q < ty, columns_to_expand)))
        ty = ty + (bty * exp_rate)

        dist_sum += (abs(tx - fx) + abs(ty - fy))

    return dist_sum


def main():
    file = open('input')
    lines = file.read().splitlines()

    arr = [[x for x in line] for line in lines]

    print(sum_distances(arr, 2 - 1))
    print(sum_distances(arr, 1000000 - 1))


if __name__ == '__main__':
    main()
