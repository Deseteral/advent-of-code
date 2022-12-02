#!/usr/local/bin/python3

def is_win(opponent, you):
    if you == "X" and opponent == "C": return 1
    if you == "Z" and opponent == "B": return 1
    if you == "Y" and opponent == "A": return 1

    if you == "X" and opponent == "A": return 0
    if you == "Y" and opponent == "B": return 0
    if you == "Z" and opponent == "C": return 0

    return -1

def calc_score(opponent, you):
    score = 0
    w = is_win(opponent, you)

    if you == "X": score += 1
    if you == "Y": score += 2
    if you == "Z": score += 3

    if w > 0: score += 6
    elif w < 0: score += 0
    elif w == 0: score += 3

    return score

with open('input') as f:
    lines = f.read().splitlines()

    total_score_a = 0
    total_score_b = 0

    for line in lines:
        (a, b) = line.split(' ')

        p = ""
        if b == "Y": # draw
            if a == "A": p = "X"
            if a == "B": p = "Y"
            if a == "C": p = "Z"
        elif b == "Z": # win
            if a == "A": p = "Y"
            if a == "B": p = "Z"
            if a == "C": p = "X"
        elif b == "X": # lose
            if a == "A": p = "Z"
            if a == "B": p = "X"
            if a == "C": p = "Y"

        total_score_a += calc_score(a, b)
        total_score_b += calc_score(a, p)

    print(total_score_a)
    print(total_score_b)
