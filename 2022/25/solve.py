#!/usr/local/bin/python3
import math

SNAFU_TO_DEC = {
    '0': 0,
    '1': 1,
    '2': 2,
    '=': -2,
    '-': -1,
}

REM_TO_SNAFU = ['0', '1', '2', '=', '-']

def from_snafu(snafu_num):
    acc = 0
    for idx, c in enumerate(reversed(snafu_num)):
        acc += SNAFU_TO_DEC[c] * math.pow(5, idx)
    return int(acc)

def to_snafu(dec):
    arr = []
    acc = dec

    while acc != 0:
        m = acc % 5
        c = REM_TO_SNAFU[m]
        arr.append(c)
        acc -= SNAFU_TO_DEC[c]
        acc //= 5

    return ''.join(reversed(arr))

def main():
    file = open('input')
    lines = file.read().splitlines()

    acc = 0
    for line in lines:
        acc += from_snafu(line)

    print(to_snafu(acc))

if __name__ == '__main__': main()
