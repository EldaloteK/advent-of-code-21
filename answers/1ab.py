#!/usr/bin/env python3

with open("../input/1a.txt", "r") as depths:
    depths_stripped = [int(number.strip()) for number in depths.readlines()]

# Part A
total_increases = sum(
    1
    for i, item in enumerate(depths_stripped)
    if i != 0 and item > depths_stripped[i - 1]
)

print(total_increases)

# Part B
total_window_increases = sum(
    1
    for i, item in enumerate(depths_stripped[:-2])
    if i != 0
    and (item + depths_stripped[i + 1] + depths_stripped[i + 2])
    > (depths_stripped[i - 1] + item + depths_stripped[i + 1])
)

print(total_window_increases)
