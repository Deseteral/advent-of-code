#!/usr/local/bin/python3

tnum_arr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
inum_arr = list(map(str, range(1, 9 + 1)))


def tnum_to_inum(tnum):
    idx = tnum_arr.index(tnum)
    return str(idx + 1)


def find_tnum(buf):
    for tnum in tnum_arr:
        if tnum in buf:
            return tnum_to_inum(tnum)
    return None


def main():
    file = open('input')
    lines = file.read().splitlines()

    # Part 1
    ss = 0
    for line in lines:
        s = list(filter(lambda x: x in inum_arr, line))
        ss += int(s[0] + s[-1])

    print(ss)

    # Part 2
    ss = 0
    for line in lines:
        first = ''
        last = ''

        # First
        buf = ''
        for c in line:
            if first: break

            if c in inum_arr:
                first = c

            buf += c
            if find_tnum(buf):
                first = find_tnum(buf)

        # Last
        buf = ''
        for c in list(reversed(line)):
            if last: break

            if c in inum_arr:
                last = c

            buf = c + buf
            if find_tnum(buf):
                last = find_tnum(buf)

        ss += int(first + last)

    print(ss)


if __name__ == '__main__':
    main()
