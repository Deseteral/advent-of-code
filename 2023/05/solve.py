#!/usr/local/bin/python3

def main():
    file = open('input')
    # file = open('test_input')
    lines = file.read().splitlines()

    # Parsing
    seeds = [int(x) for x in lines[0].split(': ')[1].split(' ')]
    categories = []

    current_category = []
    for line in list(filter(len, lines[3:])):
        if line[0].isdigit():
            dst_start, src_start, map_len = [int(x) for x in line.split(' ')]
            src_range = range(src_start, src_start + map_len)
            current_category.append((dst_start, src_range, map_len))
        else:
            categories.append(current_category)
            current_category = []
    categories.append(current_category)

    # Mapping
    def map_value_to_next_category(value, category):
        for ds, sr, _ in category:
            if value in sr:
                offset = value - sr[0]
                return ds + offset
        return value

    def map_seed_to_location(initial_value):
        value = initial_value
        for cat in categories:
            value = map_value_to_next_category(value, cat)
        return value

    # Part 1
    mapped_seeds = []
    for seed in seeds:
        mapped_seeds.append(map_seed_to_location(seed))

    print(min(mapped_seeds))

    # Part 2 (brute force)
    seed_ranges = []
    for seed_idx in range(0, len(seeds), 2):
        seed_ranges.append(range(seeds[seed_idx], seeds[seed_idx] + seeds[seed_idx + 1]))

    lowest = -1
    for r in seed_ranges:
        for seed in r:
            ms = map_seed_to_location(seed)
            if ms < lowest or lowest == -1:
                lowest = ms
                print(lowest)


if __name__ == '__main__':
    main()
