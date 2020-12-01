#!/usr/local/bin/python3

with open('input') as f:
    lines = f.read().split('\n')
    numbers = list(map(lambda x: int(x), lines))

    for i in range(len(numbers)):
        a = numbers[i]
        for j in range(i+1, len(numbers)):
            b = numbers[j]

            if (a + b) == 2020:
                two_multiplied = a * b
                print(f"two_multiplied {two_multiplied}")

            for k in range(j+1, len(numbers)):
                c = numbers[k]
                if (a + b + c) == 2020:
                    three_multiplied = a * b * c
                    print(f"three_multiplied {three_multiplied}")
