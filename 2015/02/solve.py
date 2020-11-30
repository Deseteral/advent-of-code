#!/usr/local/bin/python3

def calc_line(line_str):
    arr = line_str.split('x')
    l = int(arr[0])
    w = int(arr[1])
    h = int(arr[2])

    area = 2*l*w + 2*w*h + 2*h*l
    additional = min([l*w, w*h, h*l])

    ribbon = (sum(map(lambda x: x*2, [l, w, h])) - 2*max([l, w, h])) + (l*w*h)
    return (area + additional, ribbon)

with open('input') as f:
    lines = f.read().split('\n')

    total = 0
    ribbon_total = 0
    for line in lines:
        if line != "":
            r = calc_line(line)
            total += r[0]
            ribbon_total += r[1]

    print(f"total {total}")
    print(f"ribbon_total {ribbon_total}")
