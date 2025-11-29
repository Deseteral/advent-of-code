#!/usr/local/bin/python3
import re

with open('input') as f:
    lines = f.read().splitlines()

    passports = ['']
    for line in lines:
        if len(line) > 0:
            passports[-1] += f"{line} "
        else:
            passports.append('')

    passports = list(map(lambda x: x.strip().split(' '), passports))

    valid_count_1 = 0
    valid_count_2 = 0

    for p in passports:
        flags_1 = {
            'byr': False,
            'iyr': False,
            'eyr': False,
            'hgt': False,
            'hcl': False,
            'ecl': False,
            'pid': False,
        }

        flags_2 = {
            'byr': False,
            'iyr': False,
            'eyr': False,
            'hgt': False,
            'hcl': False,
            'ecl': False,
            'pid': False,
        }

        for field in p:
            name, value = field.split(':')

            # part 1 flags
            flags_1[name] = True

            # part 2 flags
            if name == "byr" and (1920 <= int(value) <= 2002):
                flags_2['byr'] = True
            if name == "iyr" and (2010 <= int(value) <= 2020):
                flags_2['iyr'] = True
            if name == "eyr" and (2020 <= int(value) <= 2030):
                flags_2['eyr'] = True
            if name == "hgt":
                match = re.match(r"(\d+)(cm|in)", value)
                if match != None:
                    vv, unit = match.groups()
                    if unit == "cm":
                        flags_2['hgt'] = (150 <= int(vv) <= 193)
                    elif unit == "in":
                        flags_2['hgt'] = (59 <= int(vv) <= 76)
            if name == "hcl":
                match = re.match(r"^#[a-f0-9]{6}$", value)
                flags_2['hcl'] = (match != None)
            if name == "ecl":
                flags_2['ecl'] = (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            if name == "pid":
                match = re.match(r"^\d{9}$", value)
                flags_2['pid'] = (match != None)

        if False not in flags_1.values():
            valid_count_1 += 1

        if False not in flags_2.values():
            valid_count_2 += 1

    print(f"valid_count_1 {valid_count_1}")
    print(f"valid_count_2 {valid_count_2}")
