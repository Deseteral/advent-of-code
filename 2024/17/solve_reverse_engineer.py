#!/usr/local/bin/python3
import sys


def main(input_file, _):
    input_registers, input_program = input_file.read().split('\n\n')
    input_registers = input_registers.splitlines()

    parsed_a = int(input_registers[0].split(': ')[1])
    parsed_mem = list(map(int, input_program.split(': ')[1].split(',')))

    # bst 4
    # bxl 1
    # cdv 5
    # bxc 4
    # bxl 4
    # adv 3
    # out 5
    # jnz 0

    # while A != 0:
    #     B = A % 8
    #     B = B ^ 1
    #     C = A // (2 ** B)
    #     B = B ^ C
    #     B = B ^ 4
    #     A = A // 8
    #     out += (B % 8)

    def program(input_a):
        a = input_a
        out = []
        while a != 0:
            value = (((((a % 8) ^ 1) ^ (a // (2 ** ((a % 8) ^ 1)))) ^ 4) % 8)
            out.append(value)
            a = a // 8
        return out

    # Part 1
    print(','.join(map(str, program(parsed_a))))

    # Part 2
    def match_mem_fragment(current_value, suffix_start_idx):
        mem_to_match = parsed_mem[suffix_start_idx:]
        for test_value in range(8):
            value = current_value * 8 + test_value
            if program(value) == mem_to_match:
                next_start_idx = suffix_start_idx - 1
                if next_start_idx >= 0:
                    result = match_mem_fragment(value, next_start_idx)
                    if result is not None:
                        return result
                else:
                    return value
        return None

    print(match_mem_fragment(0, len(parsed_mem) - 1))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input' if not env_test_run else 'test_input'), env_test_run)
