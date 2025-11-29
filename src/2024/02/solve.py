#!/usr/local/bin/python3

def safe_checker(levels):
    dec = True
    inc = True
    rng = True

    for idx in range(1, len(levels)):
        prev = levels[idx - 1]
        curr = levels[idx]
        diff = abs(curr - prev)
        if diff < 1 or diff > 3:
            rng = False
        if prev < curr:
            dec = False
        if prev > curr:
            inc = False

    return (dec or inc) and rng


def main():
    file = open('input')
    lines = file.read().splitlines()

    safe_count = 0
    safe_count_with_dampener = 0

    for line in lines:
        levels = [int(x) for x in line.split(' ')]

        is_safe = safe_checker(levels)
        if is_safe:
            safe_count += 1
            safe_count_with_dampener += 1
        else:
            for skip_idx in range(len(levels)):
                skip_list = levels[:skip_idx] + levels[skip_idx+1:]
                if safe_checker(skip_list):
                    safe_count_with_dampener += 1
                    break

    print(safe_count)
    print(safe_count_with_dampener)


if __name__ == '__main__':
    main()
