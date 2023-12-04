#!/usr/local/bin/python3
import functools

game_sets = []


@functools.cache
def process_card(game_idx):
    a, b = game_sets[game_idx]
    matching_numbers = len(set(a) & set(b))

    if matching_numbers == 0:
        return 0, 1
    else:
        points = pow(2, matching_numbers - 1)
        cards = 1
        for next_game_idx in range(game_idx + 1, game_idx + 1 + matching_numbers):
            if next_game_idx >= len(game_sets):
                break
            cards += process_card(next_game_idx)[1]
        return points, cards


def main():
    file = open('input')
    lines = file.read().splitlines()

    game_sets.append(())
    for line in lines:
        a, b = line.split(': ')[1].split(' | ')
        a = set(map(int, filter(len, a.split(' '))))
        b = set(map(int, filter(len, b.split(' '))))
        game_sets.append((a, b))

    total_points = 0
    total_cards = 0
    for game_idx in range(1, len(game_sets)):
        points, cards = process_card(game_idx)
        total_points += points
        total_cards += cards

    print(total_points)
    print(total_cards)


if __name__ == '__main__':
    main()
