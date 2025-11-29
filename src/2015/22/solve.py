#!/usr/local/bin/python3
from copy import deepcopy

PLAYER_WON = 1
PLAYER_LOST = 2
IN_GAME = 3

spells = [
    ('m', 53),
    ('d', 73),
    ('s', 113),
    ('p', 173),
    ('r', 229),
]

class GameState:
    def __init__(self, hp, mana, enemy_hp, enemy_damage, hard_mode):
        self.hp = hp
        self.mana = mana
        self.armor = 0
        self.mana_spent = 0
        self.next_spell = None
        self.effect_shield = 0
        self.effect_poison = 0
        self.effect_recharge = 0
        self.enemy_hp = enemy_hp
        self.enemy_damage = enemy_damage
        self.hard_mode = hard_mode

    def can_cast_spell(self, spell):
        (spell_type, cost) = spell

        if cost > self.mana: return False

        if spell_type == 'm' or spell_type == 'd': return True
        elif spell_type == 's' and self.effect_shield <= 1: return True
        elif spell_type == 'p' and self.effect_poison <= 1: return True
        elif spell_type == 'r' and self.effect_recharge <= 1: return True
        else: return False

    def cast_spell(self):
        (spell_type, cost) = self.next_spell

        self.mana -= cost
        self.mana_spent += cost

        if spell_type == 'm':
            self.enemy_hp -= 4
        elif spell_type == 'd':
            self.enemy_hp -= 2
            self.hp += 2
        elif spell_type == 's':
            self.effect_shield = 6
        elif spell_type == 'p':
            self.effect_poison = 6
        elif spell_type == 'r':
            self.effect_recharge = 5

        self.next_spell = None

    def apply_effects(self):
        self.armor = 7 if self.effect_shield > 0 else 0

        if self.effect_poison > 0:
            self.enemy_hp -= 3

        if self.effect_recharge > 0:
            self.mana += 101

        self.effect_shield -= 1
        self.effect_poison -= 1
        self.effect_recharge -= 1

    def simulate(self):
        # Player turn
        if self.hard_mode:
            self.hp -= 1
            if self.hp <= 0: return (PLAYER_LOST, [])

        self.apply_effects()
        if self.enemy_hp <= 0: return (PLAYER_WON, [])

        if self.next_spell != None: self.cast_spell()
        if self.enemy_hp <= 0: return (PLAYER_WON, [])

        castable_spells = list(filter(lambda s: self.can_cast_spell(s), spells))
        if len(castable_spells) == 0: return (PLAYER_LOST, [])

        # Enemy turn
        self.apply_effects()
        if self.enemy_hp <= 0: return (PLAYER_WON, [])

        self.hp -= max(self.enemy_damage - self.armor, 1)
        if self.hp <= 0: return (PLAYER_LOST, [])

        castable_spells = list(filter(lambda s: self.can_cast_spell(s), spells))
        return (IN_GAME, castable_spells)

def traverse(hard_mode):
    queue = []
    best_mana_cost = 9999999999

    for spell in spells:
        state = GameState(hp = 50, mana = 500, enemy_hp = 71, enemy_damage = 10, hard_mode=hard_mode)
        state.next_spell = spell
        queue.append(state)

    while len(queue) > 0:
        state = queue.pop(0)
        (play_state, castable_spells) = state.simulate()

        if play_state == PLAYER_LOST:
            continue
        elif play_state == PLAYER_WON:
            best_mana_cost = min(best_mana_cost, state.mana_spent)
            continue
        elif play_state == IN_GAME:
            for s in castable_spells:
                next_state = deepcopy(state)
                next_state.next_spell = s
                queue.append(next_state)

    print(best_mana_cost)

traverse(hard_mode=False)
traverse(hard_mode=True)
