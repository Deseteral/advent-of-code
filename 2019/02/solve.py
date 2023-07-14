#!/usr/local/bin/python3
from copy import copy
import itertools

class IntcodeVM:
    mem: list[int] = []
    pc: int = 0

    def __init__(self, initial_mem: list[int]) -> None:
        self.mem = copy(initial_mem)

    def run(self):
        while True:
            opcode = self.mem[self.pc]

            if opcode == 99:
                break
            elif opcode == 1:
                a = self.value_at_ptr(self.pc + 1)
                b = self.value_at_ptr(self.pc + 2)
                self.write_to_ptr(value=a + b, ptr=self.pc + 3)
                self.pc += 4
            elif opcode == 2:
                a = self.value_at_ptr(self.pc + 1)
                b = self.value_at_ptr(self.pc + 2)
                self.write_to_ptr(value=a * b, ptr=self.pc + 3)
                self.pc += 4
            else:
                print(f'unknown opcode {opcode}')
                return

    def value_at_ptr(self, ptr: int) -> int:
        return self.mem[self.mem[ptr]]

    def write_to_ptr(self, value: int, ptr: int) -> None:
        target = self.mem[ptr]
        self.mem[target] = value

def main():
    file = open('input')
    line = file.read().splitlines()[0]
    initial_mem = list(map(int, line.split(',')))

    # part 1
    vm = IntcodeVM(initial_mem)
    vm.mem[1] = 12
    vm.mem[2] = 2
    vm.run()
    print(vm.mem[0])

    # part 2
    for (noun, verb) in itertools.product(range(0, 99 + 1), repeat=2):
        vm = IntcodeVM(initial_mem)
        vm.mem[1] = noun
        vm.mem[2] = verb
        vm.run()

        if vm.mem[0] == 19690720:
            print(100 * noun + verb)
            break


if __name__ == '__main__': main()
