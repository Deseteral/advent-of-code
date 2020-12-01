#!/usr/local/bin/python3
import re

def inclusive_range(s, e):
    return range(s, (e+1))

def position_from_str(str):
    ss = str.split(',')
    return (int(ss[0]), int(ss[1]))

class Instruction:
    def __init__(self, action, pstart, pend):
        self.action = action
        self.pstart = pstart
        self.pend = pend

    def __repr__(self):
        return f"<{self.action} {self.pstart} {self.pend}>"

with open('input') as f:
    lines = f.read().split('\n')

    binary_screen = [[False for x in range(1000)] for y in range(1000)]
    analog_screen = [[0 for x in range(1000)] for y in range(1000)]

    instructions = []
    for line in lines:
        groups = re.match(r"^(.+) (\d+,\d+) through (\d+,\d+)$", line).groups()
        instructions.append(Instruction(groups[0], position_from_str(groups[1]), position_from_str(groups[2])))

    for ins in instructions:
        if ins.action == "turn on":
            for y in inclusive_range(ins.pstart[1], ins.pend[1]):
                for x in inclusive_range(ins.pstart[0], ins.pend[0]):
                    binary_screen[x][y] = True
                    analog_screen[x][y] += 1

        if ins.action == "turn off":
            for y in inclusive_range(ins.pstart[1], ins.pend[1]):
                for x in inclusive_range(ins.pstart[0], ins.pend[0]):
                    binary_screen[x][y] = False
                    analog_screen[x][y] = max(analog_screen[x][y] - 1, 0)

        if ins.action == "toggle":
            for y in inclusive_range(ins.pstart[1], ins.pend[1]):
                for x in inclusive_range(ins.pstart[0], ins.pend[0]):
                    binary_screen[x][y] = (not binary_screen[x][y])
                    analog_screen[x][y] += 2

    lit_count = 0
    brightness = 0
    for y in range(1000):
        for x in range(1000):
            if binary_screen[x][y] == True: lit_count += 1
            brightness += analog_screen[x][y]

    print(f"lit_count {lit_count}")
    print(f"brightness {brightness}")

