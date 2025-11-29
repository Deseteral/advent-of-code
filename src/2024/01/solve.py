#!/usr/local/bin/python3
from collections import Counter


def main():
    file = open('input')
    lines = file.read().splitlines()

    left = []
    right = []

    for line in lines:
        a, b = line.split('   ')
        left.append(int(a))
        right.append(int(b))

    left = sorted(left)
    right = sorted(right)
    right_counter = Counter(right)

    total_distance = 0
    similarity_score = 0
    for idx in range(len(left)):
        total_distance += abs(left[idx] - right[idx])
        similarity_score += left[idx] * right_counter[left[idx]]

    print(total_distance)
    print(similarity_score)


if __name__ == '__main__':
    main()
