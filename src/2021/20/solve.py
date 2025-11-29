#!/usr/local/bin/python3
from collections import Counter
from copy import deepcopy

neighbour_dir = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (0, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

def pad_image(image, flip):
    pad_size = 1
    width_after_padding = len(image) + (pad_size * 2)
    c = '#' if flip else '.'
    pad = [c for _ in range(0, pad_size)]
    full_pad = [c for _ in range(0, width_after_padding)]

    for i in range(0, len(image)):
        image[i] = [*pad, *list(image[i]), *pad]

    for _ in range(0, pad_size):
        image.append(list(full_pad))
        image.insert(0, list(full_pad))

def number_for_cell(x, y, image, flip):
    s = ''
    for dx, dy in neighbour_dir:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= len(image[0]) or ny >= len(image):
            s += '#' if flip else '.'
        else:
            s += image[ny][nx]

    s = s.replace('.', '0').replace('#', '1')
    return int(s, 2)

def enhance(image, decoder, flip=False):
    pad_image(image, flip)
    next_image = deepcopy(image)

    for y in range(0, len(image)):
        for x in range(0, len(image[0])):
            n = number_for_cell(x, y, image, flip)
            next_image[y][x] = decoder[n]

    return next_image

def count_lit_px_after(rounds, image):
    next_image = image
    for i in range(1, rounds+1):
        next_image = enhance(next_image, decoder, flip=i%2==0)

    return sum(list(map(lambda line: Counter(line)['#'], next_image)))

with open('input') as f:
    lines = f.read().splitlines()
    decoder = lines[0]
    image = lines[2:]

    # part 1
    print(count_lit_px_after(2, image))

    # part 2
    print(count_lit_px_after(50, image))
