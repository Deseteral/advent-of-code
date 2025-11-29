#!/usr/local/bin/python3

def setup_cups(inp, with_filler):
    global cups
    global current_cup
    global lowest_cup
    global highest_cup

    cups = {}
    last_connected = ''

    for idx in range(len(inp) - 1):
        cups[inp[idx]] = inp[idx + 1]
        last_connected = inp[idx + 1]

    if with_filler:
        current_filler = 10
        while len(cups) != (1000000 - 1):
            cups[last_connected] = str(current_filler)
            last_connected = str(current_filler)
            current_filler += 1

    cups[last_connected] = inp[0]

    current_cup = inp[0]
    lowest_cup = min(map(int, cups.keys()))
    highest_cup = max(map(int, cups.keys()))

def move():
    global cups
    global current_cup
    global lowest_cup
    global highest_cup

    picked_up = []

    for _ in range(3):
        next_cup = cups[current_cup]
        picked_up.append(next_cup)
        cups[current_cup] = cups[next_cup]

    destination_cup = str(int(current_cup) - 1)
    if int(destination_cup) < lowest_cup: destination_cup = str(highest_cup)

    while destination_cup in picked_up:
        destination_cup = str(int(destination_cup) - 1)
        if int(destination_cup) < lowest_cup: destination_cup = str(highest_cup)

    chain_break = cups[destination_cup]
    pu1 = picked_up.pop(0)
    pu2 = picked_up.pop(0)
    pu3 = picked_up.pop(0)
    cups[destination_cup] = pu1
    cups[pu1] = pu2
    cups[pu2] = pu3
    cups[pu3] = chain_break

    current_cup = cups[current_cup]

# init
inp = '739862541'

cups = {}
current_cup = inp[0]

# part 1
setup_cups(inp, with_filler=False)
for _ in range(100):
    move()

labels = []
gi = cups['1']
while len(labels) != (len(cups) - 1):
    labels.append(gi)
    gi = cups[gi]

print(''.join(labels))

# part 2
setup_cups(inp, with_filler=True)
for _ in range(10000000):
    move()

mm = int(cups['1']) * int(cups[cups['1']])
print(mm)
