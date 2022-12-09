#!/usr/local/bin/python3

target_coords = (2978, 3083)

max_diagonal = sum(target_coords)-1
table = [[0 for _ in range(0, max_diagonal+1)] for _ in range(0, max_diagonal+1)]

prev = table[1][1] = 20151125

for d in range(2, max_diagonal+1):
    y = d
    x = 1

    while y > 0:
        prev = table[y][x] = (prev * 252533) % 33554393
        x += 1
        y -= 1

print(table[target_coords[0]][target_coords[1]])
