#!/usr/local/bin/python3
import sys


def main(input_file, env_test_run):
    starting_values, wire_line = input_file.read().split('\n\n')

    swaps = [
        ('z31', 'mfm'),
        ('z11', 'ngr'),
        ('z06', 'fkp'),
        ('krj', 'bpt'),
    ]

    for s in swaps:
        wire_line = wire_line.replace(f'-> {s[0]}', f'-> {s[0]}_tmp')
        wire_line = wire_line.replace(f'-> {s[1]}', f'-> {s[1]}_tmp')

        wire_line = wire_line.replace(f'-> {s[0]}_tmp', f'-> {s[1]}')
        wire_line = wire_line.replace(f'-> {s[1]}_tmp', f'-> {s[0]}')

    wires = []
    for wire in wire_line.splitlines():
        a, b = wire.split(' -> ')
        a = tuple(a.split(' '))
        wires.append((a, b))

    if env_test_run:
        node_colors = {'AND': 'red', 'OR': 'green', 'XOR': 'blue', 'z-node': 'orange'}

        print('digraph {')
        print('  node [shape=rect];')
        print('  nodesep=1;')
        print('  splines=ortho;')

        for idx, ((a, op, b), v) in enumerate(wires):
            if v[0] == 'z':
                print(f'  {v} [color="{node_colors['z-node']}"];')
            else:
                print(f'  {v}')

            print(f'  op_{idx} [label="{op}" color="{node_colors[op]}"];')
            print(f'  op_{idx} -> {v};')
            print(f'  {a} -> op_{idx};')
            print(f'  {b} -> op_{idx};')

        print('}')
        return

    l = []
    for s in swaps: l += s
    print(','.join(sorted(l)))


if __name__ == '__main__':
    env_test_run = sys.argv[-1] == '-t'
    main(open('input'), env_test_run)
