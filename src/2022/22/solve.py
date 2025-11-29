#!/usr/local/bin/python3
import re

def get_row(row, level):
    return sorted(list(filter(lambda t: t[0][1] == row, level)), key=lambda t: t[0][0])

def get_column(column, level):
    return sorted(list(filter(lambda t: t[0][0] == column, level)), key=lambda t: t[0][1])

def get_at(x, y, level):
    for l in level:
        if l[0] == (x, y): return l
    return None

def get_sector_at(x, y):
    return (int(x / 50), int(y / 50))

def get_position_in_sector(x, y):
    return (int(x % 50), int(y % 50))

def did_change_sector(nx, ny, current_sector, position, direction):
    if direction[0] != 0:
        row = get_row(position[1], level)
        left_most_pos_x = row[0][0][0]
        right_most_pos_x = row[-1][0][0]

        if nx < left_most_pos_x: return True
        if nx > right_most_pos_x: return True
    else:
        column = get_column(position[0], level)
        top_most_pos_y = column[0][0][1]
        bottom_most_pos_y = column[-1][0][1]

        if ny < top_most_pos_y: return True
        if ny > bottom_most_pos_y: return True

    return current_sector != get_sector_at(nx, ny)

RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
UP = (0, -1)

directions = [RIGHT, DOWN, LEFT, UP]

def rotate_right(d):
    return directions[(directions.index(d) + 1) % len(directions)]

def rotate_left(d):
    return directions[(directions.index(d) - 1) % len(directions)]

with open('input') as f:
    lines = f.read().splitlines()

    pattern = re.findall(r"(\d+)?([A-Z])?", lines[-1])
    pattern = list(filter(lambda x: len(x) > 0, [item for sublist in pattern for item in sublist]))

    level = set()

    for y, line in enumerate(lines[:-2]):
        for x, c in enumerate(line):
            if c == '.':
                level.add(((x, y), False))
            elif c == '#':
                level.add(((x, y), True))

    def part1():
        position = get_row(0, level)[0][0]
        direction = (1, 0)

        for p in pattern:
            if p == 'R':
                direction = rotate_right(direction)
            elif p == 'L':
                direction = rotate_left(direction)
            else:
                for _ in range(int(p)):
                    nx = position[0] + direction[0]
                    ny = position[1] + direction[1]

                    if direction[0] != 0:
                        row = get_row(position[1], level)
                        left_most_pos_x = row[0][0][0]
                        right_most_pos_x = row[-1][0][0]

                        if nx < left_most_pos_x:
                            nx = right_most_pos_x
                        if nx > right_most_pos_x:
                            nx = left_most_pos_x
                    else:
                        column = get_column(position[0], level)
                        top_most_pos_y = column[0][0][1]
                        bottom_most_pos_y = column[-1][0][1]

                        if ny < top_most_pos_y:
                            ny = bottom_most_pos_y
                        if ny > bottom_most_pos_y:
                            ny = top_most_pos_y

                    nt = get_at(nx, ny, level)

                    if nt != None:
                        if nt[1] == False:
                            position = (nx, ny)
                        else:
                            break

        print(((position[0] + 1) * 4) + ((position[1] + 1) * 1000) + directions.index(direction))

    def part2():
        position = get_row(0, level)[0][0]
        direction = (1, 0)

        for p in pattern:
            if p == 'R':
                direction = rotate_right(direction)
            elif p == 'L':
                direction = rotate_left(direction)
            else:
                for _ in range(int(p)):
                    current_sector = get_sector_at(position[0], position[1])
                    current_pos_sector = get_position_in_sector(position[0], position[1])

                    nx = position[0] + direction[0]
                    ny = position[1] + direction[1]
                    nd = direction

                    if did_change_sector(nx, ny, current_sector, position, direction):
                        if current_sector == (1, 0):
                            if direction == LEFT:
                                nd = RIGHT
                                nx = 0
                                ny = (50 - current_pos_sector[1] - 1) + (2 * 50)
                            elif direction == UP:
                                nd = RIGHT
                                nx = 0
                                ny = current_pos_sector[0] + (3 * 50)

                        elif current_sector == (2, 0):
                            if direction == RIGHT:
                                nd = LEFT
                                nx = (2 * 50) - 1
                                ny = (50 - current_pos_sector[1] - 1) + (2 * 50)
                            elif direction == DOWN:
                                nd = LEFT
                                nx = (2 * 50) - 1
                                ny = current_pos_sector[0] + (1 * 50)
                            elif direction == UP:
                                nx = current_pos_sector[0]
                                ny = (4 * 50) - 1

                        elif current_sector == (1, 1):
                            if direction == RIGHT:
                                nd = UP
                                nx = current_pos_sector[1] + (2 * 50)
                                ny = (1 * 50) - 1
                            elif direction == LEFT:
                                nd = DOWN
                                nx = current_pos_sector[1]
                                ny = 2 * 50

                        elif current_sector == (0, 2):
                            if direction == LEFT:
                                nd = RIGHT
                                nx = (1 * 50)
                                ny = (50 - current_pos_sector[1] - 1)
                            elif direction == UP:
                                nd = RIGHT
                                nx = 1 * 50
                                ny = current_pos_sector[0] + (1 * 50)

                        elif current_sector == (1, 2):
                            if direction == RIGHT:
                                nd = LEFT
                                nx = (3 * 50) - 1
                                ny = (50 - current_pos_sector[1] - 1)
                            elif direction == DOWN:
                                nd = LEFT
                                nx = (1 * 50) - 1
                                ny = current_pos_sector[0] + (3 * 50)

                        elif current_sector == (0, 3):
                            if direction == RIGHT:
                                nd = UP
                                nx = current_pos_sector[1] + (1 * 50)
                                ny = (3 * 50) - 1
                            elif direction == DOWN:
                                nd = DOWN
                                nx = current_pos_sector[0] + (2 * 50)
                                ny = 0
                            elif direction == LEFT:
                                nd = DOWN
                                nx = current_pos_sector[1] + (1 * 50)
                                ny = 0

                    nt = get_at(nx, ny, level)

                    if nt != None:
                        if nt[1] == False:
                            position = (nx, ny)
                            direction = nd
                        else:
                            break

        print(((position[0] + 1) * 4) + ((position[1] + 1) * 1000) + directions.index(direction))

    part1()
    part2()
