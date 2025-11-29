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


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Parse input
    numbers = []
    symbols = []
    gear_positions = []

    for y, line in enumerate(lines):
        buf = ''
        buf_start_x = -1
        for x, ch in enumerate(line):
            if ch.isdigit():
                if buf == '': buf_start_x = x
                buf += ch
            else:
                if ch != '.':
                    symbols.append((x, y))
                    if ch == '*': gear_positions.append((x, y))
                if buf != '':
                    numbers.append((int(buf), buf_start_x, y, len(buf)))
                buf = ''

        if buf != '':
            numbers.append((int(buf), buf_start_x, y, len(buf)))

    # Calculate adjacent positions for numbers
    numbers_with_pos = []
    for number, x, y, numlen in numbers:
        positions = []
        for xx in range(x, x + numlen):
            for nx, ny in neighbour_dir:
                positions.append((xx + nx, y + ny))

        numbers_with_pos.append((number, x, y, numlen, positions))

    # Find actual part numbers
    part_numbers = []
    for number, _, _, _, numpos in numbers_with_pos:
        for pos in numpos:
            if pos in symbols:
                part_numbers.append(number)
                break

    print(sum(part_numbers))

    # Part 2
    ratio_sum = 0
    for gx, gy in gear_positions:
        gear_numbers = []
        for number, _, _, _, numpos in numbers_with_pos:
            if (gx, gy) in numpos:
                gear_numbers.append(number)

        if len(gear_numbers) == 2:
            ratio_sum += (gear_numbers[0] * gear_numbers[1])

    print(ratio_sum)


if __name__ == '__main__':
    main()
