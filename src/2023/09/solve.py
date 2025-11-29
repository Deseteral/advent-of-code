#!/usr/local/bin/python3

def main():
    file = open('input')
    lines = file.read().splitlines()

    sum_of_added_values = 0
    sum_of_added_values_back = 0

    for line in lines:
        sequences = [
            [int(x) for x in line.split(' ')]
        ]

        done = False
        while not done:
            next_seq = []
            for idx in range(1, len(sequences[-1])):
                diff = sequences[-1][idx] - sequences[-1][idx - 1]
                next_seq.append(diff)
            sequences.append(next_seq)
            if all([True if x == 0 else False for x in next_seq]):
                done = True

        sequences = list(reversed(sequences))

        # Part 1
        sequences[0].append(0)
        last_added_value = 0
        for idx in range(1, len(sequences)):
            sequence = sequences[idx]
            x = last_added_value + sequence[-1]
            sequence.append(x)
            last_added_value = x

        sum_of_added_values += last_added_value

        # Part 2
        sequences = list(map(lambda s: list(reversed(s)), sequences))

        sequences[0].append(0)
        last_added_value = 0
        for idx in range(1, len(sequences)):
            sequence = sequences[idx]
            x = sequence[-1] - last_added_value
            sequence.append(x)
            last_added_value = x

        sum_of_added_values_back += last_added_value

    print(sum_of_added_values)
    print(sum_of_added_values_back)


if __name__ == '__main__':
    main()
