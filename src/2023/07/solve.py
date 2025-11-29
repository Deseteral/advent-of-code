#!/usr/local/bin/python3
from collections import Counter
from operator import itemgetter
import itertools

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def get_strongest_hand_type(hand):
    if 'J' not in hand:
        return get_hand_type(hand)

    j_count = Counter(hand)['J']
    max_type = get_hand_type(hand)

    for j_replacements in itertools.product(cards, repeat=j_count):
        next_hand = hand
        for ridx in range(j_count):
            next_hand = next_hand.replace('J', j_replacements[ridx], 1)
        next_hand_type = get_hand_type(next_hand)
        if next_hand_type > max_type:
            max_type = next_hand_type
    return max_type


def get_hand_type(hand):
    cv = list(sorted(Counter(hand).values(), reverse=True))
    if cv == [1, 1, 1, 1, 1]:  # High card
        return 1
    elif cv == [2, 1, 1, 1]:  # One pair
        return 2
    elif cv == [2, 2, 1]:  # Two pair
        return 3
    elif cv == [3, 1, 1]:  # Three of a kind
        return 4
    elif cv == [3, 2]:  # Full house
        return 5
    elif cv == [4, 1]:  # Four of a kind
        return 6
    elif cv == [5]:  # Five of a kind
        return 7
    else:
        return 0


def calc_total_winnings(hands):
    return sum([(idx + 1) * hand[1] for idx, hand in enumerate(hands)])


def main():
    file = open('input')
    lines = file.read().splitlines()

    hands = []
    for line in lines:
        hand, bid = line.split(' ')
        bid = int(bid)
        hand_hex = hand.replace('A', 'E').replace('T', 'A').replace('J', 'B').replace('Q', 'C').replace('K', 'D')
        hand_hex_weak_joker = hand_hex.replace('B', '1')
        hand_type = get_hand_type(hand)
        hand_type_joker = get_strongest_hand_type(hand)
        hands.append((hand, bid, int(hand_hex, 16), int(hand_hex_weak_joker, 16), hand_type, hand_type_joker))

    # Part 1
    # sort by hand_type and hand_hex
    print(calc_total_winnings(sorted(hands, key=itemgetter(4, 2))))

    # Part 2
    # sort by hand_type_joker and hand_hex_weak_joker
    print(calc_total_winnings(sorted(hands, key=itemgetter(5, 3))))


if __name__ == '__main__':
    main()
