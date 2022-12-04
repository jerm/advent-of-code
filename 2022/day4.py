#!/usr/bin/env python3

total_overlaps = 0
partial_overlaps = 0

with open(f"day4.txt", "r") as fp:
    for line in fp.readlines():
        line = line.strip()
        [elf1, elf2] = line.split(",")
        elf1_range_list = elf1.split('-')
        elf2_range_list = elf2.split('-')

        elf1_range = range(int(elf1_range_list[0]), int(elf1_range_list[1]) + 1)
        elf2_range = range(int(elf2_range_list[0]), int(elf2_range_list[1]) + 1)

        union = set(elf1_range) | set(elf2_range)

        if set(elf1_range) == union or set(elf2_range) == union:
            total_overlaps +=1

        if set(elf1_range) & set(elf2_range):
            partial_overlaps +=1
print("Total Overlaps: ", total_overlaps)
print("Partial Overlaps: ", partial_overlaps)
