#!/usr/local/bin/python3
from collections import Counter

with open('input') as f:
    lines = f.read().splitlines()

    base = {}
    ingc = Counter()

    for line in lines:
        ingredients, allergens = line[:-1].split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens.split(', ')

        ingc.update(ingredients)
        for a in allergens:
            if a in base:
                base[a] = base[a].intersection(ingredients)
            else:
                base[a] = set(ingredients)

    for a in base:
        for ing in base[a]:
            if ing in ingc:
                ingc.pop(ing)

    occurences = sum(ingc.values())
    print(occurences)

    # part 2
    dang = {}
    while len(base.keys()) > 0:
        to_remove = []
        for a in base.keys():
            if len(base[a]) == 1:
                for inner_a in base.keys():
                    if a == inner_a: continue
                    base[inner_a] = base[inner_a] - base[a]
                dang[a] = base[a].pop()
                to_remove.append(a)

        for a in to_remove:
            base.pop(a, None)

    cdil = []
    for a in sorted(dang.keys()):
        cdil.append(dang[a])

    print(','.join(cdil))
