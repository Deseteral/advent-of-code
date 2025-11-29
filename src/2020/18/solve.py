#!/usr/local/bin/python3

def has_precedence(a, b):
    return op_precedence[a] >= op_precedence[b]

def pop_greater_than(ops, op):
    out = []
    while True:
        if not ops: break
        if ops[-1] not in op_precedence: break
        if not has_precedence(ops[-1], op): break
        out.append(ops.pop())
    return out

def pop_until_group_start(ops):
    out = []
    while True:
        op = ops.pop()
        if op == '(': break
        out.append(op)
    return out

def rpn(expression):
    output = []
    operators = []

    for char in expression:
        if char == '(':
            operators.append(char)
            continue

        if char == ')':
            output.extend(pop_until_group_start(operators))
            continue

        if char in op_precedence:
            output.extend(pop_greater_than(operators, char))
            operators.append(char)
            continue

        if char.isdigit():
            output.append(char)

    output.extend(reversed(operators))
    return output

def eval_rpn(expression):
    stack = []
    for val in expression:
        if val in op_precedence:
            op1 = stack.pop()
            op2 = stack.pop()
            if val == '+': result = op2 + op1
            if val == '*': result = op2 * op1
            stack.append(result)
        else:
            stack.append(int(val))

    return stack.pop()

with open('input') as f:
    lines = f.read().splitlines()

    # part 1
    op_precedence = {
        '*': 0,
        '+': 0,
    }
    sum1 = 0
    for line in lines:
        sum1 += eval_rpn(rpn(line))

    print(f"part 1 sum: {sum1}")

    # part 2
    op_precedence = {
        '*': 0,
        '+': 1,
    }
    sum2 = 0
    for line in lines:
        sum2 += eval_rpn(rpn(line))

    print(f"part 2 sum: {sum2}")
