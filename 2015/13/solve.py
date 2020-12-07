#!/usr/local/bin/python3
import itertools

# {('X', 'A'): 7, ('X', 'B'): 2, ...}
weights = {}
people = []

def calculate_happiness(guest_list):
    happiness = 0

    for i in range(len(guest_list)):
        current_guest = guest_list[i]

        if current_guest == 'Me': continue

        left_index = (i - 1)
        right_index = (i + 1)

        if left_index < 0: left_index = (len(guest_list) - 1)
        if right_index == len(guest_list): right_index = 0

        left_guest = guest_list[left_index]
        right_guest = guest_list[right_index]

        if left_guest != 'Me':
            happiness += weights[(current_guest, left_guest)]
        if right_guest != 'Me':
            happiness += weights[(current_guest, right_guest)]

    return happiness

with open('input') as f:
    lines = f.read().splitlines()

    for line in lines:
        ss = line.split(' ')
        name_from = ss[0]
        change_label = ss[2]
        change_amount = ss[3]
        name_to = ss[10][:-1]

        change_amount = int(change_amount) if change_label == 'gain' else (-1 * int(change_amount))

        weights[(name_from, name_to)] = change_amount
        people.append(name_from)

    people = set(people)

    # part 1
    permutations = list(itertools.permutations(people))

    happiness = -1
    for guest_list in permutations:
        happiness = max(happiness, calculate_happiness(guest_list))

    print(f"max happiness: {happiness}")

    # part 2
    people.add('Me')
    permutations = list(itertools.permutations(people))

    happiness_with_me = -1
    for guest_list in permutations:
        happiness_with_me = max(happiness_with_me, calculate_happiness(guest_list))

    print(f"max happiness with me: {happiness_with_me}")
