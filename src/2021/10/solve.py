#!/usr/local/bin/python3
import math
from collections import defaultdict
from collections import Counter

reverse_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
illegal_char_points_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
missing_char_points_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def check_line(line):
    stack = []

    for char in line:
        is_opening_char = char in ['(', '[', '{', '<']
        if is_opening_char:
            stack.append(char)
        else:
            expected = reverse_chars[stack.pop()]
            if expected != char:
                return (char, stack)

    return (None, stack)

with open('input') as f:
    lines = f.read().splitlines()

    illegal_occurences = defaultdict(lambda: 0)
    incomplete_lines_points = []

    for line in lines:
        incomplete_points = 0
        illegal_char, stack = check_line(line)

        if illegal_char != None:
            illegal_occurences[illegal_char] += 1

        if illegal_char == None and len(stack) > 0:
            for c in reversed(stack):
                required_char = reverse_chars[c]
                incomplete_points = (incomplete_points * 5) + missing_char_points_table[required_char]

        if incomplete_points > 0:
            incomplete_lines_points.append(incomplete_points)

    illegal_points = 0
    for char, occurence_count in Counter(illegal_occurences).items():
        illegal_points += illegal_char_points_table[char] * occurence_count
    print(f"illegal_points {illegal_points}")

    middle_idx = int(math.floor(len(incomplete_lines_points) / 2))
    incomplete_points = sorted(incomplete_lines_points)[middle_idx]
    print(f"incomplete_points {incomplete_points}")
