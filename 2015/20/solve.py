#!/usr/local/bin/python3
import math

def divisors(n):
    dvsr = set()

    for i in range(1, int(math.sqrt(n) + 1)):
        if (n % i != 0): continue
        dvsr.add(i)
        dvsr.add(int(n / i))
    return list(dvsr)

target_count = 36000000

def part1():
    house_idx = 0

    while True:
        house_idx += 1
        count = sum(divisors(house_idx)) * 10
        if count >= target_count: break

    print(house_idx)

def part2():
    houses = [0 for _ in range(target_count)]

    for elf in range(1, target_count):
        visited = 0
        for house in range(elf, target_count, elf):
            houses[house] += (elf * 11)
            visited += 1

            if visited >= 50: break

        if houses[elf] >= target_count:
            print(elf)
            break

part1()
part2()
