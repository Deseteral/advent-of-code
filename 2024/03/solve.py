#!/usr/local/bin/python3
import re


def main():
    file = open('input')
    lines = file.read().splitlines()

    total1 = 0
    total2 = 0
    enabled = True

    for line in lines:
        found = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        for s in found:
            if s == "don't()":
                enabled = False
                continue
            elif s == "do()":
                enabled = True
                continue
            else:
                a,b = s[4:-1].split(',')
                a = int(a)
                b = int(b)
                total1 += a * b
                if enabled:
                    total2 += a*b

    print(total1)
    print(total2)

if __name__ == '__main__':
    main()
