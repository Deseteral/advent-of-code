#!/usr/local/bin/python3
import sys
from collections import Counter


def generate_next_secret(initial_secret_number):
    def mix(value, secret_number):
        return value ^ secret_number

    def prune(secret_number):
        return secret_number % 16777216

    next_secret = prune(mix(initial_secret_number * 64, initial_secret_number))
    next_secret = prune(mix(next_secret // 32, next_secret))
    next_secret = prune(mix(next_secret * 2048, next_secret))
    return next_secret


def main(input_file, _):
    lines = list(map(int, input_file.read().splitlines()))

    total = 0
    best_sequences = Counter()

    for initial_secret_number in lines:
        next_secret = initial_secret_number

        prices = [
            (initial_secret_number % 10, None),
        ]

        this_seller_best_sequences = Counter()

        for step in range(2000):
            next_secret = generate_next_secret(next_secret)

            price = next_secret % 10
            price_diff = price - prices[-1][0]
            prices.append((price, price_diff))

            sequence = tuple(map(lambda p: p[1], prices[-4:]))
            if len(sequence) == 4 and sequence not in this_seller_best_sequences:
                this_seller_best_sequences[sequence] = price

        total += next_secret
        best_sequences += this_seller_best_sequences

    print(total)
    print(max(best_sequences.values()))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
