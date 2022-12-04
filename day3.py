#!/usr/bin/env python3

from functools import reduce

priorities = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total_score = 0
group_total = 0
group = []

print("Reading elf data...")

with open("day3.txt", "r") as fp:
    for line in fp.readlines():
        line = line.strip()
        first = line[:-int(len(line)/2)]
        last = line[int(len(line)/2):]
        common = list(set(first) & set(last))[0]
        total_score = total_score + priorities.index(common)
        group.append(set(line))
        if len(group) == 3:
            group.append(set(line))
            group_total = group_total + priorities.index(list(set.intersection(*group))[0])
            group = []

print("Bag Total:", total_score)
print("BadgesTotal:", group_total)
