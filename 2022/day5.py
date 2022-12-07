#!/usr/bin/env python3

import re


stacks_raw = []
moves = []
stacks = [None]
total_stacks = 0

with open(f"day5.txt", "r") as fp:
    for line in fp.readlines():
        if '[' in line:
            stacks_raw.append(line.strip("\n"))
        elif line.startswith("move"):
            moves.append(line.strip("\n"))
        elif line != "\n":
            total_stacks = int(re.sub("\s+"," ",line.strip()).split(" ")[-1])


    stacks_raw.reverse()

    for stack in range(total_stacks):
        stacks.append([])

    for raw_stack_line in stacks_raw:
        for stack in range(0, total_stacks):
            crate_slice = raw_stack_line[stack * 4:(stack*4) + 3]
            if '[' in crate_slice:
                crate = crate_slice[1]
                stacks[stack + 1].append(crate)

for move in moves:
    crates_to_move = []
    move_split = move.split(" ")
    num_crates = int(move_split[1])
    source = int(move_split[3])
    target = int(move_split[5])
    for count in range(num_crates):
        crates_to_move.append(stacks[source].pop())
    for count in range(num_crates):
        stacks[target].append(crates_to_move.pop())


top_crates = ""
for stack in stacks[1:]:
    crate = stack.pop()
    top_crates = f"{top_crates}{crate}"

print(top_crates)
