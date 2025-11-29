#!/usr/local/bin/python3

def count_bits_in_position(values, position):
    ones = 0
    zeroes = 0

    for line in values:
        bit = line[position]
        if bit == '1': ones += 1
        if bit == '0': zeroes += 1

    return (ones, zeroes)

def calculate_power_consumption(lines):
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(lines[0])):
        ones, zeroes = count_bits_in_position(lines, i)

        if ones > zeroes:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    gamma_decimal = int(gamma_rate, 2)
    epsilon_decimal = int(epsilon_rate, 2)

    return gamma_decimal * epsilon_decimal

def calculate_life_support_rating(lines):
    oxygen_values = lines

    for i in range(len(lines[0])):
        ones, zeroes =  count_bits_in_position(oxygen_values, i)

        if ones >= zeroes:
            oxygen_values = list(filter(lambda x: x[i] == '1', oxygen_values))
        else:
            oxygen_values = list(filter(lambda x: x[i] == '0', oxygen_values))

        if len(oxygen_values) == 1: break


    co2_values = lines

    for i in range(len(lines[0])):
        ones, zeroes = count_bits_in_position(co2_values, i)

        if zeroes <= ones:
            co2_values = list(filter(lambda x: x[i] == '0', co2_values))
        else:
            co2_values = list(filter(lambda x: x[i] == '1', co2_values))

        if len(co2_values) == 1: break


    oxygen_rating = int(oxygen_values[0], 2)
    co2_rating = int(co2_values[0], 2)
    return oxygen_rating * co2_rating

with open('input') as f:
    lines = f.read().splitlines()

    power_consumption = calculate_power_consumption(lines)
    print(f"power_consumption {power_consumption}")

    life_support_rating = calculate_life_support_rating(lines)
    print(f"life_support_rating {life_support_rating}")

