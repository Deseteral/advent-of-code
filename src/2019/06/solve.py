#!/usr/local/bin/python3
from collections import defaultdict

def main():
    file = open('input')
    lines = file.read().splitlines()

    d = defaultdict(lambda: None)

    d['COM'] = None
    for line in lines:
        l, r = line.split(')')
        d[r] = l

    ss = defaultdict(lambda: -1)

    def cnt(key):
        if key == 'COM':
            return 0

        if ss[key] != -1:
            return ss[key]

        v = cnt(d[key]) + 1
        ss[key] = v
        return v

    print(sum(map(lambda k: cnt(k), d.keys())))

    # part 2
    you = d['YOU']
    san = d['SAN']
    visited = defaultdict(lambda: 99999)
    queue = [(you, 0)]

    while len(queue) > 0:
        nn, jmp = queue.pop()
        visited[nn] = jmp

        parent = d[nn]
        if parent not in visited:
            queue.append((parent, jmp + 1))

        for dk in d.keys():
            if d[dk] == nn and dk not in visited:
                queue.append((dk, jmp + 1))

    print(visited[san])

if __name__ == '__main__': main()
