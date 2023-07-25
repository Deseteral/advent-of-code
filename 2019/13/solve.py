#!/usr/local/bin/python3
import itertools
from copy import copy
from collections import defaultdict
from collections import Counter

def parse_mem(line: str) -> list[int]:
    return list(map(int, line.split(',')))

def get_digit(number: int, n: int) -> int:
    return number // 10**n % 10

class IntcodeVM:
    def __init__(self, initial_mem: list[int], memory_size = 1_000_000) -> None:
        self.mem: list[int] = [0] * memory_size
        for idx in range(len(initial_mem)):
            self.mem[idx] = initial_mem[idx]

        self.pc: int = 0
        self.input: list[int] = []
        self.output: list[int] = []
        self.halted = False
        self.piped_buffers: list[list[int]] = []
        self.relative_base = 0

    def run(self):
        while not self.halted: self.tick()

    def tick(self):
        instruction = self.mem[self.pc]
        opcode = instruction % 100
        modes = [None, get_digit(instruction, 2), get_digit(instruction, 3), get_digit(instruction, 4)]

        if opcode == 99: # halt
            self.halted = True
            return
        elif opcode == 1: # add
            a = self.deref(self.pc + 1, modes[1])
            b = self.deref(self.pc + 2, modes[2])
            self.write_to_mem(value=a + b, ptr=self.pc + 3, mode=modes[3])
            self.pc += 4
        elif opcode == 2: # mul
            a = self.deref(self.pc + 1, modes[1])
            b = self.deref(self.pc + 2, modes[2])
            self.write_to_mem(value=a * b, ptr=self.pc + 3, mode=modes[3])
            self.pc += 4
        elif opcode == 3: # input
            if len(self.input) == 0:
                return
            v = self.input.pop()
            self.write_to_mem(value=v, ptr=self.pc + 1, mode=modes[1])
            self.pc += 2
        elif opcode == 4: # output
            v = self.deref(self.pc + 1, modes[1])
            self.output.append(v)
            for buffer in self.piped_buffers:
                buffer.insert(0, v)
            self.pc += 2
        elif opcode == 5: # jump-if-true
            v = self.deref(self.pc + 1, modes[1])
            jmp_target = self.deref(self.pc + 2, modes[2])
            if v != 0:
                self.pc = jmp_target
            else:
                self.pc += 3
        elif opcode == 6: # jump-if-false
            v = self.deref(self.pc + 1, modes[1])
            jmp_target = self.deref(self.pc + 2, modes[2])
            if v == 0:
                self.pc = jmp_target
            else:
                self.pc += 3
        elif opcode == 7: # less than
            a = self.deref(self.pc + 1, modes[1])
            b = self.deref(self.pc + 2, modes[2])
            self.write_to_mem(value=1 if a < b else 0, ptr=self.pc + 3, mode=modes[3])
            self.pc += 4
        elif opcode == 8: # equals
            a = self.deref(self.pc + 1, modes[1])
            b = self.deref(self.pc + 2, modes[2])
            self.write_to_mem(value=1 if a == b else 0, ptr=self.pc + 3, mode=modes[3])
            self.pc += 4
        elif opcode == 9: # relative base offset
            v = self.deref(self.pc + 1, modes[1])
            self.relative_base += v
            self.pc += 2
        else:
            print(f'unknown opcode {opcode}')

    def deref(self, ptr: int, mode: int) -> int:
        if mode == 0: # position mode
            return self.mem[self.mem[ptr]]
        elif mode == 1: # immediate mode
            return self.mem[ptr]
        elif mode == 2: # relative mode
            return self.mem[self.mem[ptr] + self.relative_base]
        else:
            print(f'unknown mode: {mode}')

    def write_to_mem(self, value: int, ptr: int, mode: int) -> None:
        if mode == 0: # position mode
            self.mem[self.mem[ptr]] = value
        elif mode == 2: # relative mode
            self.mem[self.mem[ptr] + self.relative_base] = value
        else:
            print(f'unsupported mode: {mode}')

    def pipe(self, buffer: list[int]) -> None:
        self.piped_buffers.append(buffer)

    def send_input(self, value: int) -> None:
        self.input.insert(0, value)

    def print_output(self, last_value: bool = False) -> None:
        if last_value: print(self.output[-1])
        else: print(self.output)

def main():
    file = open('input')
    lines = file.read().splitlines()
    initial_mem = parse_mem(lines[0])

    # part 1
    vm = IntcodeVM(initial_mem)
    vm.run()

    print(Counter(vm.output[2::3])[2])

if __name__ == '__main__': main()
