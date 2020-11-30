#!/usr/local/bin/python3

with open('input') as f:
    s = f.read()
    level = 0
    basement_flag = False
    basement_instruction = -1

    for i in range(len(s)):
        ch = s[i]
        if ch == '(':
            level += 1
        elif ch == ')':
            level -= 1

        if level == -1 and basement_flag == False:
            basement_flag = True
            basement_instruction = i+1

    print(f"level {level}")
    print(f"basement_instruction {basement_instruction}")
