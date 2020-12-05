#!/usr/local/bin/python3
import re
import math

def bsp(seat_from, seat_len, lower_char, upper_char, code):
    for c in code:
        if c == lower_char:
            seat_len = math.floor(seat_len / 2)
        elif c == upper_char:
            seat_from += (math.floor(seat_len / 2) + 1)
            seat_len = math.floor(seat_len / 2)
    return seat_from

with open('input') as f:
    lines = f.read().splitlines()

    ids = []
    for line in lines:
        row = line[:7]
        column = line[7:]

        row = bsp(0, 127, 'F', 'B', line[:7])
        column = bsp(0, 7, 'L', 'R', line[7:])

        seat_id = row * 8 + column
        ids.append(seat_id)

    print(f"highest seat ID: {max(ids)}")

    ids = sorted(ids)
    for i in range(len(ids) - 1):
        if (ids[i+1] - ids[i]) > 1:
            print(f"your seat ID: {ids[i] + 1}")
