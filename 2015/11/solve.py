#!/usr/local/bin/python3

def next_char(char):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if char == 'z':
        return 'a'
    else:
        return letters[letters.index(char) + 1]

def next_password(password):
    password = list(password)[::-1] # reverse
    i = 0

    while i < len(password):
        nc = next_char(password[i])
        password[i] = nc
        if nc == 'a':
            i += 1
        else:
            break
    return ''.join(password[::-1])

def has_increasing_three(password):
    for i in range(len(password) - 2):
        if (ord(password[i]) + 2) == (ord(password[i + 1]) + 1) == (ord(password[i + 2])):
            return True
    return False

def has_forbidden_chars(password):
    return 'i' in password or 'o' in password or 'l' in password

def has_double_pair(password):
    pair_count = 0
    i = 0
    while i < (len(password) - 1):
        if password[i] == password[i + 1]:
            pair_count += 1
            i += 1
        i += 1

    return pair_count == 2

def is_valid_pass(password):
    return has_increasing_three(password) and not has_forbidden_chars(password) and has_double_pair(password)

def search_next_pass(current_pass):
    while True:
        current_pass = next_password(current_pass)
        if is_valid_pass(current_pass):
            return current_pass

next_pass = search_next_pass('cqjxjnds')
print(f"next_pass: {next_pass}")
next_next_pass = search_next_pass(next_pass)
print(f"next_next_pass: {next_next_pass}")
