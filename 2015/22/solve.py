#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy
import random
from sre_constants import IN

spells = [
    ('m', 53),
    ('d', 73),
    ('s', 113),
    ('p', 173),
    ('r', 229),
]

PLAYER_WIN = 1
PLAYER_LOSE = 2
IN_GAME = 3

class GameState:
    def __init__(self, hp = 50, mana = 500, arm = 0, mana_spent = 0, next_spell = None, e_shield = 0, e_poison = 0, e_recharge = 0, ehp = 71, edmg = 10, hard_mode = False):
        self.hp = hp
        self.mana = mana
        self.arm = arm
        self.mana_spent = mana_spent
        self.next_spell = next_spell
        self.e_shield = e_shield
        self.e_poison = e_poison
        self.e_recharge = e_recharge
        self.ehp = ehp
        self.edmg = edmg
        self.hard_mode = hard_mode

    def __copy__(self):
        print('heleoh')
        return type(self)(self.hp, self.mana, self.arm, self.mana_spent, self.next_spell, self.e_shield, self.e_poison, self.e_recharge, self.ehp, self.edmg, self.hard_mode)

    def can_cast_spell(self, spell):
        (spell_type, cost) = spell

        if cost > self.mana: return False

        if (spell_type == 'm' or spell_type == 'd'): return True
        elif spell_type == 's' and self.e_shield <= 0: return True
        elif spell_type == 'p' and self.e_poison <= 0: return True
        elif spell_type == 'r' and self.e_recharge <= 0: return True
        else: return False

    def cast_spell(self, spell):
        (spell_type, cost) = spell

        self.mana -= cost
        self.mana_spent += cost

        if spell_type == 'm':
            self.ehp -= 4
        elif spell_type == 'd':
            self.ehp -= 2
            self.hp += 2
        elif spell_type == 's':
            self.e_shield = 6
        elif spell_type == 'p':
            self.e_poison = 6
        elif spell_type == 'r':
            self.e_recharge = 5

    def apply_effects(self):
        self.arm = 7 if self.e_shield > 0 else 0

        # print('Shields timer is now', (self.e_shield - 1))

        if self.e_poison > 0:
            self.ehp -= 3
            # print('Poison deals 3 damage; its timer is now', (self.e_poison - 1))

        if self.e_recharge > 0:
            self.mana += 101
            # print('Recharge provides 101 mana; its timer is now', (self.e_recharge - 1))

        self.e_shield -= 1
        self.e_poison -= 1
        self.e_recharge -= 1

    def simulate(self):
        global spells

        # Player turn

        # print('-- Player turn --')
        # print('- Player has', self.hp, 'hit points', self.arm, 'armor', self.mana, 'mana')
        # print('- Boss has', self.ehp, 'hit points')
        # print('')

        if self.hard_mode:
            self.hp -= 1
            if self.hp <= 0: return (PLAYER_LOSE, [])

        self.apply_effects()

        self.cast_spell(self.next_spell)
        # print('Casting', self.next_spell)
        self.next_spell = None

        castable_spells = list(filter(lambda s: self.can_cast_spell(s), spells))

        if len(castable_spells) == 0:
            # print('No more spells')
            return (PLAYER_LOSE, [])

        if self.ehp <= 0:
            print('helo')
            return (PLAYER_WIN, [])

        # Enemy turn

        # print('')
        # print('-- Boss turn --')
        # print('- Player has', self.hp, 'hit points', self.arm, 'armor', self.mana, 'mana')
        # print('- Boss has', self.ehp, 'hit points')
        # print('')

        self.apply_effects()

        attack_value = max(self.edmg - self.arm, 1)
        self.hp -= attack_value

        # print('Boss attacks for', attack_value, 'damage!')

        if self.hp <= 0:
            return (PLAYER_LOSE, [])

        return (IN_GAME, castable_spells)

def part1():
    queue = []
    best_mana_cost = 9999999999

    for spell in spells:
        state = GameState(False)
        state.next_spell = spell
        queue.append(state)

    while len(queue) > 0:
        # print(len(queue))

        state = queue.pop()
        (play_state, castable_spells) = state.simulate()

        if play_state == PLAYER_LOSE:
            continue
        elif play_state == PLAYER_WIN:
            best_mana_cost = min(best_mana_cost, state.mana_spent)
            continue
        elif play_state == IN_GAME:
            print(len(castable_spells))
            for s in castable_spells:
                # next_state = deepcopy(state)
                next_state = state.copy()
                next_state.next_spell = s
                queue.append(next_state)

    print('best_mana_cost', best_mana_cost)

part1()

# For part 2:
# state = GameState(True)


# 1824 is part 1 answer
