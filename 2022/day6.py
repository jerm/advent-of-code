#!/usr/bin/env python3

pos = 0
my_slice = []

with open(f"day6.txt", "r") as fp:
    stream = fp.read()

for pos in range(len(stream)):
    my_slice.append(stream[pos])
    if len(my_slice) == 14:
        if len(set(my_slice)) == 14:
            print(my_slice)
            print(pos+1)
        else:
            my_slice.pop(0)

