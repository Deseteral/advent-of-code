#!/usr/local/bin/python3
import math

def main():
    file = open('input')
    lines = map(int, file.read().splitlines())

    s = 0
    s2 = 0

    for mass in lines:
        required_fuel = (math.floor(mass / 3) - 2)
        s += required_fuel

        additional_fuel = 0
        r = required_fuel
        while r > 0:
            r = (math.floor(r / 3) - 2)
            additional_fuel += max(r, 0)

        s2 += (required_fuel + additional_fuel)

    print(s)
    print(s2)

if __name__ == '__main__': main()
