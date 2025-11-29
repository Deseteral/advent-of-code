#!/usr/local/bin/python3
from collections import defaultdict

with open('input') as f:
    lines = f.read().splitlines()

    count = 0
    sum = 0

    for line in lines:
        input_value, output_value = list(map(lambda x: x.strip(), line.split('|')))
        inputs = input_value.split(' ')
        outputs = output_value.split(' ')

        # part 1
        for digit in outputs:
            ld = len(digit)
            if ld == 2 or ld == 3 or ld == 4 or ld == 7:
                count += 1

        # part 2
        mappings = defaultdict(lambda: [])

        for segment_config in inputs:
            ld = len(segment_config)
            if ld == 2: mappings['1'] = segment_config
            elif ld == 3: mappings['7'] = segment_config
            elif ld == 4: mappings['4'] = segment_config
            elif ld == 7: mappings['8'] = segment_config

        mappings['6'] = next(
            filter(
                lambda x: set(mappings['1']).issubset(x) == False,
                filter(lambda x: len(x) == 6, inputs)
            )
        , None)

        mappings['3'] = next(
            filter(
                lambda x: set(mappings['1']).issubset(x),
                filter(lambda x: len(x) == 5, inputs)
            )
        , None)

        # difference betwen 0 and 9
        a = set(filter(lambda x: len(x) == 6, inputs)) - set([mappings['6']])
        aa = a.pop()
        bb = a.pop()

        c = (set(aa) - set(bb)).pop()
        if c in mappings['4']:
            mappings['9'] = aa
            mappings['0'] = bb
        else:
            mappings['9'] = bb
            mappings['0'] = aa

        # difference betwen 2 and 5
        z = set(filter(lambda x: len(x) == 5, inputs)) - set([mappings['3']])
        zz = z.pop()
        xx = z.pop()

        if len(set(mappings['9']) - set(zz)) == 2:
            mappings['2'] = zz
            mappings['5'] = xx
        else:
            mappings['2'] = xx
            mappings['5'] = zz

        # end of mappings
        reverse_mappings = {v: k for k, v in mappings.items()}

        str_value = ''
        for digit in outputs:
            k = next(filter(lambda x: set(x) == set(digit), reverse_mappings.keys()), None)
            str_value += reverse_mappings[k]

        sum += int(str_value)

    print(f"count {count}")
    print(f"sum {sum}")
