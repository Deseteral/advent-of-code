#!/usr/local/bin/python3

with open('input') as f:
    lines = f.read().splitlines()
    numbers = list(map(lambda x: int(x), lines))

    # part 1

    increased_count = 0
    prev_num = -1

    for num in numbers:
        if num > prev_num and prev_num != -1:
            increased_count += 1

        prev_num = num

    print(f"increased_count {increased_count}")

    # part 2

    increased_sum_count = 0
    prev_sum = -1

    for i in range(2, len(numbers)):
        sum = numbers[i - 2] + numbers[i - 1] + numbers[i]

        if sum > prev_sum and prev_sum != -1:
            increased_sum_count += 1

        prev_sum = sum

    print(f"increased_sum_count {increased_sum_count}")
