#!/usr/bin/env python3

with open("../input/2ab.txt", "r") as depth_positions:
    positions = [movement.strip().split() for movement in depth_positions.readlines()]

position_map = {
    "up": (
        lambda current_position, depth_decrease: current_position - depth_decrease
    ),
    "down": (
        lambda current_position, depth_increase: current_position + depth_increase
    ),
    "forward": (
        lambda current_position, move: current_position + move
    ),
}

# Part A
position_totals = {"up": 0, "down": 0, "forward": 0}

for i, item in enumerate(positions):
    position_totals[item[0]] = position_map[item[0]](
        int(position_totals[item[0]]), int(item[1])
    )

total = (position_totals["up"] + position_totals["down"]) * position_totals["forward"]

print(total)

# Part B
aim_depth_totals = {"up": 0, "down": 0, "forward": 0, "depth": 0}

for i, item in enumerate(positions):
    aim_depth_totals[item[0]] = position_map[item[0]](
        int(aim_depth_totals[item[0]]), int(item[1])
    )
    if item[0] == "forward":
        aim_depth_totals["depth"] = (
            aim_depth_totals["up"] + aim_depth_totals["down"]
        ) * int(item[1]) + aim_depth_totals["depth"]

total_depth_aim = aim_depth_totals["depth"] * aim_depth_totals["forward"]

print(total_depth_aim)
