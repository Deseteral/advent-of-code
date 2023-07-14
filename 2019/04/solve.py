#!/usr/local/bin/python3

def main():
    in_from = 145852
    in_to = 616942

    p1_count = 0
    p2_count = 0

    for value in range(in_from, in_to + 1):
        n = list(map(int, str(value)))

        adj = False
        adj_lg = False
        dec = True

        adj_streak = 1

        for idx in range(1, len(n)):
            if n[idx] < n[idx-1]:
                dec = False
                break

            if n[idx] == n[idx-1]:
                adj = True

            if n[idx] == n[idx-1]:
                adj_streak += 1
            else:
                if adj_streak == 2: adj_lg = True
                adj_streak = 1

        if adj_streak == 2: adj_lg = True

        if dec:
            if adj: p1_count += 1
            if adj_lg: p2_count += 1

    print(p1_count)
    print(p2_count)

if __name__ == '__main__': main()
