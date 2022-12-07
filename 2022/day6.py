#!/usr/bin/env python3

pos = 0
my_slice = []
marker_length = 14

with open(f"day6.txt", "r") as fp:
    stream = fp.read()

for pos in range(len(stream)):
    my_slice.append(stream[pos])
    if len(my_slice) == marker_length:
        if len(set(my_slice)) == marker_length:
            print(my_slice)
            print(pos+1)
        else:
            my_slice.pop(0)

