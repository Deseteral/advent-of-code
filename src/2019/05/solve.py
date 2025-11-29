#!/usr/local/bin/python3
from copy import copy

def get_digit(number: int, n: int) -> int:
    return number // 10**n % 10

class IntcodeVM:
    def __init__(self, initial_mem: list[int]) -> None:
        self.mem: list[int] = copy(initial_mem)
        self.pc: int = 0
        self.input: int | None = None
        self.output: list[int] = []

    def run(self):
        while True:
            instruction = self.mem[self.pc]
            opcode = instruction % 100
            modes = [None, get_digit(instruction, 2), get_digit(instruction, 3), get_digit(instruction, 4)]

            if opcode == 99: # halt
                break
            elif opcode == 1: # add
                a = self.deref(self.pc + 1, modes[1])
                b = self.deref(self.pc + 2, modes[2])
                self.write_to_mem(value=a + b, ptr=self.pc + 3)
                self.pc += 4
            elif opcode == 2: # mul
                a = self.deref(self.pc + 1, modes[1])
                b = self.deref(self.pc + 2, modes[2])
                self.write_to_mem(value=a * b, ptr=self.pc + 3)
                self.pc += 4
            elif opcode == 3: # input
                self.write_to_mem(value=self.input, ptr=self.pc + 1)
                self.pc += 2
            elif opcode == 4: # output
                v = self.deref(self.pc + 1, modes[1])
                self.output.append(v)
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
                self.write_to_mem(value=1 if a < b else 0, ptr=self.pc + 3)
                self.pc += 4
            elif opcode == 8: # equals
                a = self.deref(self.pc + 1, modes[1])
                b = self.deref(self.pc + 2, modes[2])
                self.write_to_mem(value=1 if a == b else 0, ptr=self.pc + 3)
                self.pc += 4
            else:
                print(f'unknown opcode {opcode}')
                return

    def deref(self, ptr: int, mode: int) -> int:
        if mode == 0: # position mode
            return self.mem[self.mem[ptr]]
        elif mode == 1: # immediate mode
            return self.mem[ptr]
        else:
            print(f'unknown mode: {mode}')

    def write_to_mem(self, value: int, ptr: int) -> None:
        target = self.mem[ptr]
        self.mem[target] = value

def main():
    file = open('input')
    line = file.read().splitlines()[0]
    initial_mem = list(map(int, line.split(',')))

    # part 1
    vm = IntcodeVM(initial_mem)
    vm.input = 1
    vm.run()
    print(vm.output[-1])

    # part 2
    vm = IntcodeVM(initial_mem)
    vm.input = 5
    vm.run()
    print(vm.output[-1])

if __name__ == '__main__': main()
