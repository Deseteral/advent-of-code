#!/usr/local/bin/python3

def word_vowel_count(word):
    vowel_count = 0
    for ch in word:
        if ch in "aeiou":
            vowel_count += 1
    return vowel_count

def word_has_letter_twice(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return True
    return False

def word_has_forbidden_string(word):
    for i in range(len(word) - 1):
        if f"{word[i]}{word[i+1]}" in ["ab", "cd", "pq", "xy"]:
            return True
    return False

def word_contains_two_seq(word):
    for i in range(len(word) - 1):
        seq = f"{word[i]}{word[i+1]}"
        for j in range(i+2, len(word) - 1):
            next_seq = f"{word[j]}{word[j+1]}"
            if seq == next_seq:
                return True
    return False

def word_letter_repeats_in_between(word):
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            return True
    return False


def is_nice_1(str):
    a = word_vowel_count(str) >= 3
    b = word_has_letter_twice(str)
    c = word_has_forbidden_string(str)
    return a and b and not c

def is_nice_2(str):
    a = word_contains_two_seq(str)
    b = word_letter_repeats_in_between(str)
    return a and b

with open('input') as f:
    lines = f.read().split('\n')

    nice_count_1 = 0
    nice_count_2 = 0

    for line in lines:
        if is_nice_1(line):
            nice_count_1 += 1
        if is_nice_2(line):
            nice_count_2 += 1

    print(f"nice_count_1 {nice_count_1}")
    print(f"nice_count_2 {nice_count_2}")
