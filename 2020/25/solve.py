#!/usr/local/bin/python3

def crack_loop_size(public_key):
    subject_number = 7
    loop_size = 1
    value = 1

    while True:
        value *= subject_number
        value = value % 20201227
        if value == public_key: break
        loop_size += 1

    return loop_size

def transform(subject_number, loop_size):
    value = 1

    for _ in range(loop_size):
        value *= subject_number
        value = value % 20201227

    return value

with open('input') as f:
    card_public_key, door_public_key = [int(x) for x in f.read().splitlines()]

    card_loop_size = crack_loop_size(card_public_key)
    door_loop_size = crack_loop_size(door_public_key)

    print(f"card_loop_size: {card_loop_size}, door_loop_size: {door_loop_size}")

    encryption_key_1 = transform(door_public_key, card_loop_size)
    encryption_key_2 = transform(card_public_key, door_loop_size)

    assert (encryption_key_1 == encryption_key_2),"Encryption keys don't match up"

    print(f"encryption_key: {encryption_key_1}")
