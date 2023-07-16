#!/usr/local/bin/python3
import itertools
from copy import copy

def parse_mem(line: str) -> list[int]:
    return list(map(int, line.split(',')))

def get_digit(number: int, n: int) -> int:
    return number // 10**n % 10

class IntcodeVM:
    def __init__(self, initial_mem: list[int]) -> None:
        self.mem: list[int] = copy(initial_mem)
        self.pc: int = 0
        self.input: list[int] = []
        self.output: list[int] = []
        self.halted = False
        self.piped_buffers: list[list[int]] = []

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
            self.write_to_mem(value=a + b, ptr=self.pc + 3)
            self.pc += 4
        elif opcode == 2: # mul
            a = self.deref(self.pc + 1, modes[1])
            b = self.deref(self.pc + 2, modes[2])
            self.write_to_mem(value=a * b, ptr=self.pc + 3)
            self.pc += 4
        elif opcode == 3: # input
            if len(self.input) == 0:
                return
            v = self.input.pop()
            self.write_to_mem(value=v, ptr=self.pc + 1)
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
            self.write_to_mem(value=1 if a < b else 0, ptr=self.pc + 3)
            self.pc += 4
        elif opcode == 8: # equals
            a = self.deref(self.pc + 1, modes[1])
            b = self.deref(self.pc + 2, modes[2])
            self.write_to_mem(value=1 if a == b else 0, ptr=self.pc + 3)
            self.pc += 4
        else:
            print(f'unknown opcode {opcode}')

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

    def pipe(self, buffer: list[int]) -> None:
        self.piped_buffers.append(buffer)

    def send_input(self, value: int) -> None:
        self.input.insert(0, value)

def main():
    file = open('input')
    lines = file.read().splitlines()
    initial_mem = parse_mem(lines[0])

    # part 1
    highest_signal = -1
    for phase_setting_sequence in itertools.permutations(range(0, 4+1), 5):
        input_value = 0
        for idx in range(5):
            vm = IntcodeVM(initial_mem)
            vm.input = [input_value, phase_setting_sequence[idx]]
            vm.run()
            input_value = vm.output[-1]

        highest_signal = max(input_value, highest_signal)

    print(highest_signal)

    # part 2
    highest_signal = -1
    for phase_setting_sequence in itertools.permutations(range(5, 9+1), 5):
        vm_list = list(map(lambda _: IntcodeVM(initial_mem), range(5)))

        for idx in range(5):
            vm_list[idx].send_input(phase_setting_sequence[idx])

        vm_list[0].send_input(0)

        for idx in range(5):
            current_vm = vm_list[idx]
            next_vm = vm_list[(idx + 1) % 5]
            current_vm.pipe(next_vm.input)

        while not vm_list[-1].halted:
            for vm in vm_list: vm.tick()

        highest_signal = max(vm_list[-1].output[-1], highest_signal)

    print(highest_signal)


if __name__ == '__main__': main()
