#!/usr/local/bin/python3

def simple_processing(course):
    pos = 0
    depth = 0

    for command, amount in course:
        if command == 'forward':
            pos += amount
        elif command == 'up':
            depth -= amount
        elif command == 'down':
            depth += amount

    return pos * depth

def processing(course):
    pos = 0
    depth = 0
    aim = 0

    for command, amount in course:
        if command == 'forward':
            pos += amount
            depth += aim * amount
        elif command == 'up':
            aim -= amount
        elif command == 'down':
            aim += amount

    return pos * depth

with open('input') as f:
    lines = f.read().splitlines()
    course = []

    for line in lines:
        arr = line.split(' ')
        course.append((arr[0], int(arr[1])))

    print(f"simple_processing {simple_processing(course)}")
    print(f"processing {processing(course)}")
