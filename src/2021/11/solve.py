#!/usr/local/bin/python3

neighbour_dir = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def is_valid_pos(x, y, grid):
    if x < 0 or y < 0: return False
    if x >= len(grid[0]) or y >= len(grid): return False
    return True

with open('input') as f:
    lines = f.read().splitlines()

    grid = [
        [int(x) for x in line] for line in lines
    ]
    grid_size = len(grid) * len(grid[0])

    flash_count = 0
    all_flashed = False

    for step in range(1, 1000 + 1):
        # First, the energy level of each octopus increases by 1.
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                grid[y][x] += 1

        # any octopus with an energy level greater than 9 flashes.
        flashed = []
        could_flash = True

        while could_flash:
            could_flash = False
            for y in range(0, len(grid)):
                for x in range(0, len(grid[y])):
                    if grid[y][x] <= 9 or (x, y) in flashed: continue

                    flash_count += 1
                    flashed.append((x, y))
                    could_flash = True

                    for dx, dy in neighbour_dir:
                        nx = x + dx
                        ny = y + dy
                        if is_valid_pos(nx, ny, grid): grid[ny][nx] += 1

        # any octopus that flashed during this step has its energy level set to 0
        for x, y in flashed:
            grid[y][x] = 0

        # Winning conditions
        if step == 100:
            print(f"Flash count on step 100: {flash_count}")

        if len(flashed) == grid_size and not all_flashed:
            print(f"All flashed on step: {step}")
            all_flashed = True

        if step > 100 and all_flashed: break
