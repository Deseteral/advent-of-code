#!/usr/local/bin/python3
import itertools

with open('input') as f:
    numbers = [int(x) for x in f.read().splitlines()]

    # part 1
    break_number = None
    start_idx = 0
    while True:
        previous_numbers = numbers[start_idx:(start_idx + 25)]
        break_number = numbers[start_idx + 25]

        if not break_number in map(sum, itertools.combinations(previous_numbers, 2)):
            break
        start_idx += 1

    print(f"break_number {break_number}")

    # part 2
    for s, e in itertools.product(range(len(numbers)), range(len(numbers))):
        if (e - s) < 2: continue

        contiguous_set = numbers[s:e]
        if (sum(contiguous_set) == break_number):
            encryption_weakness = min(contiguous_set) + max(contiguous_set)
            print(f"encryption_weakness {encryption_weakness}")
            break
