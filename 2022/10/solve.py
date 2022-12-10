#!/usr/local/bin/python3

with open('input') as f:
    lines = f.read().splitlines()

    x = 1
    cycle = 0

    checks = range(20, 220 + 1, 40)
    signals = []

    screen = ['' for _ in range(0, 240 + 1)]

    def next_cycle():
        global x, cycle, screen
        cycle += 1

        if cycle in checks: signals.append(cycle * x)

        idx = cycle-1
        screen[idx] = '#' if (idx % 40) in (x-1, x, x+1) else '.'

    for line in lines:
        next_cycle()
        if line == 'noop': continue

        for _ in range(0, 1): next_cycle()
        x += int(line.split(' ')[1])

    # part 1
    print(sum(signals), end='\n\n')

    # part 2
    for y in range(0, 6):
        for x in range(0, 40):
            print(screen[x + (y * 40)], end='')
        print('')
