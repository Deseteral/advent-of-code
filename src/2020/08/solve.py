#!/usr/local/bin/python3
import re
import math
from collections import defaultdict
import itertools

class VM:
    def __init__(self, program):
        self.pc = 0
        self.acc = 0
        self.program = program
        self.done = False

    def tick(self):
        if self.pc == len(self.program):
            self.done = True
            return

        curr = self.program[self.pc]

        if curr['times_executed'] > 0:
            self.done = True
            return

        opcode, value = curr['instr']
        if opcode == 'acc':
            self.acc += value
        if opcode == 'jmp':
            self.pc += (value - 1)

        curr['times_executed'] += 1
        self.pc += 1

    def run(self):
        while not self.done:
            self.tick()

        if self.pc == len(self.program):
            return 0
        else:
            return 1

def load_program_from_file():
    with open('input') as f:
        lines = f.read().splitlines()

        program = []
        for line in lines:
            opcode, value = line.split(' ')
            program.append({ 'instr': (opcode, int(value)), 'times_executed': 0 })
        return program

# part 1
program = load_program_from_file()
vm = VM(program)
vm.run()
print(f"acc after executed_twice: {vm.acc}")

# part 2
def run_after_pachting(program):
    vm = VM(program)
    exit_code = vm.run()
    if exit_code == 0:
        print(f"acc after patching: {vm.acc}")

for i in range(len(program)):
    curr_opcode = program[i]['instr'][0]

    if curr_opcode == 'jmp':
        patched_program = load_program_from_file()
        patched_program[i]['instr'] = ('nop', 0)
        run_after_pachting(patched_program)

    if curr_opcode == 'nop':
        patched_program = load_program_from_file()
        patched_program[i]['instr'] = ('jmp', patched_program[i]['instr'][1])
        run_after_pachting(patched_program)
