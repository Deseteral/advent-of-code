#!/usr/local/bin/python3
import sys


class VM:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.mem = []
        self.pc = 0
        self.output = []

    def tick(self):
        opcode = self.mem[self.pc]
        self.pc += 1
        operand = self.mem[self.pc]
        self.pc += 1

        if opcode == 0:
            self.adv(operand)
        elif opcode == 1:
            self.bxl(operand)
        elif opcode == 2:
            self.bst(operand)
        elif opcode == 3:
            self.jnz(operand)
        elif opcode == 4:
            self.bxc(operand)
        elif opcode == 5:
            self.out(operand)
        elif opcode == 6:
            self.bdv(operand)
        elif opcode == 7:
            self.cdv(operand)

    def run(self):
        while self.pc < len(self.mem):
            self.tick()

    def adv(self, operand):
        numerator = self.A
        denominator = 2 ** self.combo_operand(operand)
        self.A = int(numerator / denominator)

    def bxl(self, operand):
        self.B = self.B ^ operand

    def bst(self, operand):
        self.B = self.combo_operand(operand) % 8

    def jnz(self, operand):
        if self.A == 0:
            return
        self.pc = operand

    def bxc(self, operand):
        self.B = self.B ^ self.C

    def out(self, operand):
        self.output.append(self.combo_operand(operand) % 8)

    def bdv(self, operand):
        numerator = self.A
        denominator = 2 ** self.combo_operand(operand)
        self.B = int(numerator / denominator)

    def cdv(self, operand):
        numerator = self.A
        denominator = 2 ** self.combo_operand(operand)
        self.C = int(numerator / denominator)

    def combo_operand(self, operand):
        return [0, 1, 2, 3, self.A, self.B, self.C][operand]

    def __repr__(self):
        return f"VM state\n  A: {self.A}\n  B: {self.B}\n  C: {self.C}\n  mem: {self.mem}\n  out: {self.output}\n"


def main(input_file, _):
    input_registers, input_program = input_file.read().split('\n\n')
    input_registers = input_registers.splitlines()

    parsed_a = int(input_registers[0].split(': ')[1])
    parsed_b = int(input_registers[1].split(': ')[1])
    parsed_c = int(input_registers[2].split(': ')[1])
    parsed_mem = list(map(int, input_program.split(': ')[1].split(',')))

    # Part 1
    vm = VM()
    vm.A = parsed_a
    vm.B = parsed_b
    vm.C = parsed_c
    vm.mem = parsed_mem[:]

    vm.run()
    print(','.join(map(str, vm.output)))

    # Part 2
    # I did part 2 by looking at how different A values change output memory.
    # Then I could estimate the value that produces the required output.

    # start_a = parsed_a * 759310
    # start_a = 202992820304670 - 3518436
    start_a = 202992818072106 - 1
    while True:
        # print(next_a)
        vm = VM()
        vm.A = start_a
        vm.B = parsed_b
        vm.C = parsed_c
        vm.mem = parsed_mem[:]
        vm.run()
        # print(vm.output)
        # if vm.output[:8] == parsed_mem[:8]:
        #     print(f"aaa: {start_a}")

        # backoff = 11
        # if vm.output[-backoff:] == parsed_mem[-backoff:]:
        if vm.output == parsed_mem:
            print(f"aaa: {start_a}")
        start_a -= 1


# 202992818072106 is too high


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
