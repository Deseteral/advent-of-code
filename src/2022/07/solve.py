#!/usr/local/bin/python3

class Entity:
    def __init__(self, type, size, path, parent):
        self.type = type
        self.size = size
        self.path = path
        self.parent = parent

with open('input') as f:
    lines = f.read().splitlines()

    entities = [
        Entity('d', -1, '/', None)
    ]

    # parsing
    path = []
    for line in lines:
        if line[0] == '$':
            if line == '$ cd /': path = []
            elif line == '$ cd ..': path.pop()
            elif line == '$ ls': continue
            else:
                next_dir = line.split(' ')[2]
                path.append(next_dir)
        else:
            is_dir = line[:3] == 'dir'
            entity_name = None
            size = -1

            if is_dir:
                entity_name = line.split(' ')[1]
            else:
                entity_name = line.split(' ')[1]
                size = int(line.split(' ')[0])

            parent = '/'.join(['', *path]) if len(path) > 0 else '/'
            entity_path = '/'.join(['', *path, entity_name])
            entity = Entity('d' if is_dir else 'f', size, entity_path, parent)

            entities.append(entity)

    # processing
    all_dirs = list(filter(lambda e: e.type == 'd', entities))
    dirs_to_process = list([*all_dirs])

    while len(dirs_to_process) > 0:
        current_dir = dirs_to_process.pop(0)

        children = list(filter(lambda e: e.parent == current_dir.path, entities))
        has_unknown_size_children = len(list(filter(lambda e: e.size == -1, children))) > 0

        if has_unknown_size_children:
            dirs_to_process.append(current_dir)
        else:
            current_dir.size = sum(list(map(lambda e: e.size, children)))

    # part 1
    all_dir_sizes = list(map(lambda e: e.size, all_dirs))
    print(sum(list(filter(lambda size: size <= 100000, all_dir_sizes))))

    # part 2
    unused_space = 70000000 - entities[0].size
    need_space = 30000000 - unused_space
    print(min(list(filter(lambda size: size >= need_space, all_dir_sizes))))
