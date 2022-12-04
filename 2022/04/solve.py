#!/usr/local/bin/python3

with open('input') as f:
    lines = f.read().splitlines()

    count_a = 0
    count_b = 0

    for line in lines:
        (a, b) = line.split(',')
        (al, ar) = map(lambda x: int(x), a.split('-'))
        (bl, br) = map(lambda x: int(x), b.split('-'))

        if al <= bl and ar >= br:
            count_a += 1
        elif bl <= al and br >= ar:
            count_a += 1

        for aa in range(al, ar+1):
            if aa in range(bl, br+1):
                count_b += 1
                break

    print(count_a)
    print(count_b)
