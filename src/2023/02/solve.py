#!/usr/local/bin/python3


def main():
    file = open('input')
    lines = file.read().splitlines()

    game_ids_sum = 0
    sum_set_powers = 0

    for line_idx, line in enumerate(lines):
        game_id = (line_idx + 1)

        max_r = -1
        max_g = -1
        max_b = -1

        for game_set in line.split(': ')[1].split('; '):
            for color_set in game_set.split(', '):
                amount = int(color_set.split(' ')[0])
                if 'red' in color_set:
                    max_r = max(max_r, amount)
                elif 'green' in color_set:
                    max_g = max(max_g, amount)
                elif 'blue' in color_set:
                    max_b = max(max_b, amount)

        if max_r <= 12 and max_g <= 13 and max_b <= 14:
            game_ids_sum += game_id

        sum_set_powers += (max_r * max_g * max_b)

    print(game_ids_sum)
    print(sum_set_powers)


if __name__ == '__main__':
    main()
