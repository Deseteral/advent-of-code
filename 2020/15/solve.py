#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
from collections import Counter
import itertools
from copy import deepcopy

age = 0
numbers = defaultdict(lambda: '0')
last = ''
next_age = ''

def next_number():
    global age
    global numbers
    global last
    global next_age

    age += 1
    last_age = next_age

    if next_age == '0':
        last = '0'
    else:
        last = str((age - 1) - int(next_age))

    next_age = numbers[last]
    numbers[last] = age

# input data import
in_num = "1,17,0,10,18,11,6".split(',')

for n in in_num:
    age += 1
    next_age = numbers[n]
    last = n
    numbers[n] = str(age)

# part 1
while age < 2020:
    next_number()

print(f"after 2020 turns: {last}")

# part 2
while age < 30000000:
    next_number()

print(f"after 30000000 turns: {last}")
