#!/usr/local/bin/python3
from collections import Counter

class Tree:
    def __init__(self, size):
        self.size = size

        self.max_top = size
        self.max_right = size
        self.max_bottom = size
        self.max_left = size

        self.top_visible = False
        self.right_visible = False
        self.bottom_visible = False
        self.left_visible = False

        self.score_top = 0
        self.score_right = 0
        self.score_bottom = 0
        self.score_left = 0

    def is_visible(self):
        return self.top_visible == True or self.right_visible == True or self.bottom_visible == True or self.left_visible == True

    def calc_score(self):
        return self.score_top * self.score_right * self.score_bottom * self.score_left

with open('input') as f:
    lines = f.read().splitlines()

    size = len(lines[0])
    level = [[Tree(int(x)) for x in line] for line in lines]

    # part 1
    # mark edges
    for x in range(0, size):
        level[0][x].top_visible = True
        level[size-1][x].bottom_visible = True

    for y in range(0, size):
        level[y][0].left_visible = True
        level[y][size-1].right_visible = True

    # mark middle
    for y in range(1, size-1):
        # from left to right
        for x in range(1, size-1):
            current = level[y][x]
            left = level[y][x-1]
            if left.max_left < current.size:
                current.left_visible = True
            else:
                current.max_left = left.max_left

        # from right to left
        for x in range(size-2, 0, -1):
            current = level[y][x]
            right = level[y][x+1]
            if right.max_right < current.size:
                current.right_visible = True
            else:
                current.max_right = right.max_right

    for x in range(1, size-1):
        # from top to bottom
        for y in range(1, size-1):
            current = level[y][x]
            top = level[y-1][x]
            if top.max_top < current.size:
                current.top_visible = True
            else:
                current.max_top = top.max_top

        # from bottom to top
        for y in range(size-2, 0, -1):
            current = level[y][x]
            bottom = level[y+1][x]
            if bottom.max_bottom < current.size:
                current.bottom_visible = True
            else:
                current.max_bottom = bottom.max_bottom

    # part 2
    for y in range(0, size):
        for x in range(0, size):
            current = level[y][x]

            # left
            for xx in range(x-1, -1, -1):
                current.score_left += 1
                if level[y][xx].size >= current.size: break

            # right
            for xx in range(x+1, size):
                current.score_right += 1
                if level[y][xx].size >= current.size: break

            # top
            for yy in range(y-1, -1, -1):
                current.score_top += 1
                if level[yy][x].size >= current.size: break

            # bottom
            for yy in range(y+1, size):
                current.score_bottom += 1
                if level[yy][x].size >= current.size: break

    # visibility count
    flat_level = [tree for row in level for tree in row]

    visibility_counter = Counter(list(map(lambda tree: tree.is_visible(), flat_level)))
    print(visibility_counter[True])

    # score count
    score = max(list(map(lambda tree: tree.calc_score(), flat_level)))
    print(score)
