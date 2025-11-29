#!/usr/local/bin/python3
import functools


@functools.cache
def solve(springs, checks):
    # When there is no more springs and no more checks we're good
    if len(springs) == 0:
        return 1 if len(checks) == 0 else 0

    # When the checks are empty and there are no more not working springs we're good
    if len(checks) == 0:
        return 1 if '#' not in springs else 0

    current_char = springs[0]
    possibilites = 0

    # Skip working spring
    if current_char == '.' or current_char == '?':
        possibilites += solve(springs[1:], checks)

    # Start new group
    if current_char == '#' or current_char == '?':
        current_check = checks[0]
        current_group = springs[:current_check]

        if '.' not in current_group:  # Group can be continuous
            if len(springs) == current_check and len(checks) == 1:  # This is the last group
                possibilites += 1

            # The group ends with working spring (or ? that could be replaced with one)
            # then advance the calculations after that separator
            if len(springs) > current_check:
                if springs[current_check] == '.' or springs[current_check] == '?':
                    possibilites += solve(springs[current_check + 1:], checks[1:])

    return possibilites


def main():
    file = open('input')
    lines = file.read().splitlines()

    total = 0
    total_unfolded = 0

    for line in lines:
        springs, checks = line.split(' ')
        checks = tuple(int(x) for x in checks.split(','))

        spings_unfolded = springs
        checks_unfolded = checks
        for _ in range(4):
            spings_unfolded += ('?' + springs)
            checks_unfolded = (*checks_unfolded, *checks)

        total += solve(springs, checks)
        total_unfolded += solve(spings_unfolded, checks_unfolded)

    print(total)
    print(total_unfolded)


if __name__ == '__main__':
    main()
