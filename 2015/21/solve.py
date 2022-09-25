#!/usr/local/bin/python3
import itertools

def simulate(dmg, arm):
    ehp = 109
    edmg = 8
    earm = 2

    hp = 100

    while True:
        ehp -= max(dmg - earm, 1)
        if ehp <= 0: return True

        hp -= max(edmg - arm, 1)
        if hp <= 0: return False

shop = [
    # Type  Cost  Damage  Armor
    # 0     1     2       3
    ('w', 8, 4, 0),
    ('w', 10, 5, 0),
    ('w', 25, 6, 0),
    ('w', 40, 7, 0),
    ('w', 74, 8, 0),

    ('a', 0, 0, 0),
    ('a', 13, 0, 1),
    ('a', 31, 0, 2),
    ('a', 53, 0, 3),
    ('a', 75, 0, 4),
    ('a', 102, 0, 5),

    ('r1', 0, 0, 0),
    ('r1', 25, 1, 0),
    ('r1', 50, 2, 0),
    ('r1', 100, 3, 0),
    ('r1', 20, 0, 1),
    ('r1', 40, 0, 2),
    ('r1', 80, 0, 3),

    ('r2', 0, 0, 0),
    ('r2', 25, 1, 0),
    ('r2', 50, 2, 0),
    ('r2', 100, 3, 0),
    ('r2', 20, 0, 1),
    ('r2', 40, 0, 2),
    ('r2', 80, 0, 3),
]

lowest_cost_to_win = 9999999999
highest_cost_to_lose = 0

for c in itertools.combinations(shop, 4):
    if len(set(map(lambda x: x[0], c))) != 4: continue

    r1_cost = next(x for x in c if x[0] == 'r1')[1]
    r2_cost = next(x for x in c if x[0] == 'r2')[1]

    if (r1_cost != 0 and r2_cost != 0) and (r1_cost == r2_cost): continue

    cost = sum(map(lambda x: x[1], c))
    dmg = sum(map(lambda x: x[2], c))
    arm = sum(map(lambda x: x[3], c))

    player_did_win = simulate(dmg, arm)

    if player_did_win:
        lowest_cost_to_win = min(lowest_cost_to_win, cost)
    else:
        highest_cost_to_lose = max(highest_cost_to_lose, cost)

print('lowest_cost_to_win', lowest_cost_to_win)
print('highest_cost_to_lose', highest_cost_to_lose)
