#!/usr/local/bin/python3

def calc_score(player1, player2):
    winning_deck = player1 if len(player1) > 0 else player2
    score = 0
    for idx, card in enumerate(reversed(winning_deck)):
        score += card * (idx + 1)
    return score

def play_round(player1, player2):
    cp1 = player1.pop(0)
    cp2 = player2.pop(0)

    res = 0
    if len(player1) >= cp1 and len(player2) >= cp2:
        res = recursive_combat(player1[0:cp1], player2[0:cp2])
    else:
        res = 1 if cp1 > cp2 else 2

    if res == 1:
        player1.append(cp1)
        player1.append(cp2)
    else:
        player2.append(cp2)
        player2.append(cp1)

def recursive_combat(player1, player2):
    rounds = []
    while True:
        round_id = (player1.copy(), player2.copy())
        if round_id in rounds:
            return 1
        rounds.append(round_id)

        play_round(player1, player2)

        res = 0
        if len(player1) == 0: res = 2
        elif len(player2) == 0: res = 1

        if res != 0: return res

def combat(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        cp1 = player1.pop(0)
        cp2 = player2.pop(0)

        if cp1 > cp2:
            player1.append(cp1)
            player1.append(cp2)
        else:
            player2.append(cp2)
            player2.append(cp1)

with open('input') as f:
    player1, player2 = f.read().split('\n\n')
    player1 = [int(x) for x in player1.splitlines()[1:]]
    player2 = [int(x) for x in player2.splitlines()[1:]]

    combat_deck_1 = player1.copy()
    combat_deck_2 = player2.copy()
    combat(combat_deck_1, combat_deck_2)
    print(f"combat score: {calc_score(combat_deck_1, combat_deck_2)}")

    r_combat_deck_1 = player1.copy()
    r_combat_deck_2 = player2.copy()
    recursive_combat(r_combat_deck_1, r_combat_deck_2)
    print(f"combat score: {calc_score(r_combat_deck_1, r_combat_deck_2)}")
