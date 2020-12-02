#!/usr/local/bin/python3
import re

with open('input') as f:
    lines = f.read().splitlines()

    correct_count_1 = 0
    correct_count_2 = 0

    for line in lines:
        groups = re.match(r"(\d+)-(\d+) (\w): (\w+)$", line).groups()
        lmin, lmax, letter, password = groups
        lmin = int(lmin)
        lmax = int(lmax)

        count = password.count(letter)
        if lmin <= count <= lmax:
            correct_count_1 += 1

        in_pos_1 = (password[lmin - 1] == letter)
        in_pos_2 = (password[lmax - 1] == letter)
        if (in_pos_1 and not in_pos_2) or (not in_pos_1 and in_pos_2):
            correct_count_2 += 1


    print(f"correct_count_1 {correct_count_1}")
    print(f"correct_count_2 {correct_count_2}")
