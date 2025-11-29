#!/usr/local/bin/python3
import math

parsed_packets_versions = []

def hex_to_bin(hex):
    mm = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    num_s = ''
    for c in hex: num_s += mm[c]
    return num_s

def parse_packet(packet):
    print('')

    packet_version = int(packet[:3], 2)
    parsed_packets_versions.append(packet_version)
    print('packet_version', packet_version)

    packet_type = int(packet[3:6], 2)
    is_literal_packet = (packet_type == 4)
    print('packet_type', packet_type, 'literal' if is_literal_packet else 'operator')

    if is_literal_packet:
        keep_going = True
        idx = 6
        number_bin = ''
        while keep_going:
            group = packet[idx:idx+5]
            keep_going = group[0] == '1'
            bits = group[1:]
            idx += 5
            number_bin += bits
        number_dec = int(number_bin, 2)
        print('literal_number', number_dec)

        total_packet_length = idx
        print('total_packet_length', total_packet_length)
        return (idx, number_dec)
    else: # operator packet
        length_type_id = packet[6]
        print('length_type_id', length_type_id)

        subpacket_results = []
        total_bits_used = 0

        if length_type_id == '0':
            subpackets_bits_count = int(packet[7:7+15], 2)
            print('subpackets_bits_count', subpackets_bits_count)
            subpackets_bits = packet[7+15:7+15+subpackets_bits_count]

            idx = 0
            while idx < subpackets_bits_count:
                used_bits_count, subpacket_result = parse_packet(subpackets_bits)
                subpacket_results.append(subpacket_result)
                idx += used_bits_count
                subpackets_bits = subpackets_bits[used_bits_count:]
            total_bits_used = 7+15+subpackets_bits_count
        else: # number_of_subpackets
            subpacket_count = int(packet[7:7+11], 2)
            print('subpacket_count', subpacket_count)
            idx = 0
            for _ in range(subpacket_count):
                subpacket = packet[7+11+idx:]
                used_bits_count, subpacket_result = parse_packet(subpacket)
                subpacket_results.append(subpacket_result)
                idx += used_bits_count
            total_bits_used = 7+11+idx

        result = 0
        if packet_type == 0: result = sum(subpacket_results)
        if packet_type == 1: result = math.prod(subpacket_results)
        if packet_type == 2: result = min(subpacket_results)
        if packet_type == 3: result = max(subpacket_results)
        if packet_type == 5: result = 1 if subpacket_results[0] > subpacket_results[1] else 0
        if packet_type == 6: result = 1 if subpacket_results[0] < subpacket_results[1] else 0
        if packet_type == 7: result = 1 if subpacket_results[0] == subpacket_results[1] else 0

        return (total_bits_used, result)

with open('input') as f:
    lines = f.read().splitlines()

    packet = hex_to_bin(lines[0])
    _, result = parse_packet(packet)

    print('\n---\n')

    packet_version_sum = sum(parsed_packets_versions)
    print('packet_version_sum', packet_version_sum)

    print('result', result)
