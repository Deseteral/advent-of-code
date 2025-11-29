#!/usr/local/bin/python3

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")

class Shape:
    def __init__(self, pos, fields):
        self.pos = pos
        self.fields = fields

    def fields_in_world_space(self):
        return set(map(lambda v: self.pos + v, self.fields))

    def check_collision(self, level):
        for f in self.fields_in_world_space():
            if f.x < 0 or f.x >= 7:
                return True
            if f.y < 0:
                return True
            if f in level:
                return True

        return False

def h_line_shape(pos):
    return Shape(pos, set([ Vec2(0, 0), Vec2(1, 0), Vec2(2, 0), Vec2(3, 0) ]))

def plus_shape(pos):
    return Shape(pos, set([ Vec2(0, 1), Vec2(1, 1), Vec2(2, 1), Vec2(1, 0), Vec2(1, 2) ]))

def l_shape(pos):
    return Shape(pos, set([ Vec2(0, 0), Vec2(1, 0), Vec2(2, 0), Vec2(2, 1), Vec2(2, 2) ]))

def v_line_shape(pos):
    return Shape(pos, set([ Vec2(0, 0), Vec2(0, 1), Vec2(0, 2), Vec2(0, 3) ]))

def square_shape(pos):
    return Shape(pos, set([ Vec2(0, 0), Vec2(1, 0), Vec2(0, 1), Vec2(1, 1) ]))

STATE_NEW_ROCK = 1
STATE_FALLING = 2
STATE_STATE_PUSHING = 3

def simulate(target, pattern):
    level = set()

    highest_rock = 0
    state = STATE_NEW_ROCK
    active_rock = None
    next_shape = [h_line_shape, plus_shape, l_shape, v_line_shape, square_shape]
    next_shape_idx = 0
    pattern_idx = 0
    stopped_rocks = 0

    skip_first_cycle = True

    while True:
        if pattern_idx == 0 and next_shape_idx == 4 and state == STATE_NEW_ROCK:
            if skip_first_cycle:
                skip_first_cycle = False
            else:
                iters = int((1000000000000-stopped_rocks) / 1725)

                stopped_rocks += 1725 * iters
                highest_rock += 2630 * iters

                partition_amount = 16
                current_highest_rock = max(list(map(lambda v: v.y, level))) + 1
                diff = highest_rock - current_highest_rock
                level = set(list(
                    map(
                        lambda v: Vec2(v.x, v.y + diff),
                        filter(lambda v: v.y > current_highest_rock - partition_amount, level)
                    )
                ))

        if state == STATE_NEW_ROCK:
            active_rock = next_shape[next_shape_idx](Vec2(2, highest_rock + 3))
            next_shape_idx += 1
            if next_shape_idx >= len(next_shape): next_shape_idx = 0
            state = STATE_STATE_PUSHING

        elif state == STATE_STATE_PUSHING:
            direction = pattern[pattern_idx]
            pattern_idx += 1
            if pattern_idx >= len(pattern): pattern_idx = 0

            original_pos = active_rock.pos
            active_rock.pos += Vec2(1, 0) if direction == '>' else Vec2(-1, 0)

            if active_rock.check_collision(level):
                active_rock.pos = original_pos

            state = STATE_FALLING

        elif state == STATE_FALLING:
            original_pos = active_rock.pos
            active_rock.pos += Vec2(0, -1)

            if active_rock.check_collision(level):
                active_rock.pos = original_pos
                for f in active_rock.fields_in_world_space(): level.add(f)

                highest_rock = max(list(map(lambda v: v.y, level))) + 1
                stopped_rocks += 1

                if stopped_rocks == target: return highest_rock
                state = STATE_NEW_ROCK
            else:
                state = STATE_STATE_PUSHING

with open('input') as f:
    lines = f.read().splitlines()
    pattern = lines[0]

    print(simulate(2022, pattern))
    print(simulate(1000000000000, pattern))
