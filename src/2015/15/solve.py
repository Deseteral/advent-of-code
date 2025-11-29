#!/usr/local/bin/python3

bestscore = 0
bestscore_500 = 0

for s in range(100 + 1):
    for p in range(100 + 1):
        for f in range(100 + 1):
            for ss in range(100 + 1):
                if ((s + p + f + ss) != 100): continue

                capacity = max(((5 * s) + (-1 * p) + (0 * f) + (-1 * ss)), 0)
                durability = max(((-1 * s) + (3 * p) + (-1 * f) + (0 * ss)), 0)
                flavor = max(((0 * s) + (0 * p) + (4 * f) + (0 * ss)), 0)
                texture = max(((0 * s) + (0 * p) + (0 * f) + (2 * ss)), 0)

                calories = (s * 5) + (p * 1) + (f * 6) + (ss * 8)

                score = capacity * durability * flavor * texture

                bestscore = max(bestscore, score)
                if (calories == 500): bestscore_500 = max(bestscore_500, score)

print(bestscore)
print(bestscore_500)
