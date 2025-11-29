#!/usr/local/bin/python3
import sys
from itertools import islice


def part1(line):
    disk = []

    block_id = 0
    for idx, char in enumerate(line):
        is_free_space = idx % 2 != 0
        if is_free_space:
            disk.extend([None] * int(char))
        else:
            disk.extend([block_id] * int(char))
            block_id += 1

    for idx in range(len(disk) - 1, -1, -1):
        block_id = disk[idx]
        if block_id is None:
            continue

        disk[disk.index(None)] = block_id
        disk[idx] = None

        if all(map(lambda e: e is None, islice(disk, disk.index(None), len(disk)))):
            break

    checksum = 0
    for idx in range(disk.index(None)):
        checksum += idx * disk[idx]

    print(checksum)


def part2(line):
    disk = []

    block_id = 0
    for idx in range(len(line)):
        size = int(line[idx])
        is_free_space = idx % 2 != 0
        if is_free_space:
            disk.append((None, size, True))
        else:
            disk.append((block_id, size, False))
            block_id += 1

    while not all(map(lambda e: e[2] == True, disk)):
        for idx in range(len(disk) - 1, -1, -1):
            block_id, size, visited = disk[idx]

            if visited:
                continue

            disk[idx] = (block_id, size, True)

            for free_idx in range(idx):
                current_block_id, current_size, _ = disk[free_idx]

                can_swap = current_block_id is None and current_size >= size
                if can_swap:
                    disk[idx] = (None, size, True)
                    disk[free_idx] = (block_id, size, True)

                    remaining_space = current_size - size
                    if remaining_space > 0:
                        disk.insert(free_idx + 1, (None, remaining_space, True))

                    break

    extended_disk = []
    for (block_id, size, _) in disk:
        extended_disk.extend([block_id] * size)

    checksum = 0
    for idx, block_id in enumerate(extended_disk):
        if block_id is None: continue
        checksum += idx * block_id

    print(checksum)


def main(input_file):
    line = input_file.read().splitlines()[0]
    part1(line)
    part2(line)


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'))
