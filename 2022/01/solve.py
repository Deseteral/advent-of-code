#!/usr/local/bin/python3

with open('input') as f:
    lines = f.read().splitlines()

    acc = 0
    elves = []

    for line in lines:
        if line == "":
            elves.append(acc)
            acc = 0
        else:
            acc += int(line)

    elves.sort(reverse=True)

    print(elves[0])
    print(sum(elves[:3]))
