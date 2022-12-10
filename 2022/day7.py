#!/usr/bin/env python3

import copy

from flexdict import FlexDict

fs = FlexDict()
dir_stack = []
prev_dir = []
total_size = 0
disk = 70000000
necessary_free = 30000000
fs["/", "size"] = 0
with open("day7.txt", "r") as fp:
    for entry in fp.readlines():
        entry = entry.strip().split(' ')
        if entry[0] == "$":
            if entry[1] == "cd":
                if entry[2] == "..":
                    subdir_size = fs[dir_stack,'size']
                    dir_stack.pop()
                    fs[dir_stack,'size'] += subdir_size
                else:
                    dir_stack.append(entry[2])
                    spaces = ""
                    for i in dir_stack:
                        spaces = spaces + "   "
                    if fs[dir_stack,'size'] != 0:
                        exit(1)
            if entry[1] == 'ls':
                continue
        elif entry[0] == 'dir':
            fs[dir_stack,entry[1], 'size'] = 0
        else:
            fs[dir_stack,'size'] += int(entry[0])
    while dir_stack:
        subdir_size = fs[dir_stack,'size']
        dir_stack.pop()
        if dir_stack:
            fs[dir_stack,'size'] += subdir_size


used_space =  fs['/', 'size']
free_space =  disk - fs['/', 'size']
need_to_free = necessary_free - free_space
best_size = used_space
best_dir = ""
flat = fs.flatten()
for dir_item in flat:
    dir_name = dir_item[0][-2]
    size = dir_item[1]
    if size >= need_to_free:
        if size < best_size:
            best_size = size
            best_dir = dir_name

print("best dir to delete is", best_dir, best_size)
