#!/usr/local/bin/python3
from collections import defaultdict
from collections import Counter

def print_dots(dots):
    for y in range(0, 15):
        for x in range(0, 50):
            print('#' if dots[(x, y)] else '.', end='')
        print('\n', end='')
    print('')

def do_fold(fold, dots):
    fold_axis, fold_line = fold
    if fold_axis == 'y':
        below_fold_positions = list(filter(
            lambda pos: dots[pos] and pos[1] > fold_line,
            dots.keys(),
        ))
        for pos in below_fold_positions:
            next_pos = (pos[0], fold_line - (pos[1] - fold_line))
            dots[pos] = False
            dots[next_pos] = True

    if fold_axis == 'x':
        right_fold_positions = list(filter(
            lambda pos: dots[pos] and pos[0] > fold_line,
            dots.keys(),
        ))
        for pos in right_fold_positions:
            next_pos = (fold_line - (pos[0] - fold_line), pos[1])
            dots[pos] = False
            dots[next_pos] = True

with open('input') as f:
    lines = f.read().splitlines()

    # parsing input
    dots = defaultdict(lambda: False)
    folds = []

    for line in lines:
        if len(line) == 0: continue
        if 'fold' in line:
            lhs, rhs = line.split('=')
            folds.append((lhs[-1], int(rhs)))
        else:
            pos = list(map(lambda x: int(x), line.split(',')))
            dots[(pos[0], pos[1])] = True

    # first fold
    do_fold(folds[0], dots)
    print(f"dots count after first fold: {Counter(dots.values())[True]}", end='\n\n')

    # rest of folding
    for fold in folds[1:]:
        do_fold(fold, dots)

    print_dots(dots)
