#!/usr/bin/env python3

elves = [0, 0]
cur_elf = 1
cur_elf_total = 0
max_elf = 1

print("Reading elf data...")

with open("day1.txt", "r") as fp:
    for line in fp.readlines():
        line = line.strip()
        if line == '':
            elves[cur_elf] = cur_elf_total
            if cur_elf_total > elves[max_elf]:
                max_elf = cur_elf
            cur_elf_total = 0
            cur_elf += 1
            elves.append(0)

        else:
            cur_elf_total += int(line)

print(f"The elf carrying the most calories is elf:{max_elf}, with {elves[max_elf]} calories")

elves.sort()
top_elves_total = 0
for counter in [1,2,3]:
    top_elves_total += elves.pop()

print(f"The total of the top 3 elves is: {top_elves_total}")
