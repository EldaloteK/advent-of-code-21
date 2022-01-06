#!/usr/bin/env python3

with open("../input/9ab.txt", "r") as report:
    initial_lines = [[int(k.strip()) for k in r.strip()] for r in report.readlines()]

board_length = len(initial_lines[0])

allCoordinates = {(i, c):initial_lines[i][c] for i in range(len(initial_lines)) for c in range(board_length)}

# Part A
total_a = 0
lowest_values = {}
all_adjacent_values = {}

for line_index, line in enumerate(initial_lines):
    for position in range(board_length):
        surrounding_coords = []
        temp_surrounding_coords = []
        for (k,v) in [(line_index-1, position), (line_index+1, position), (line_index, position-1), (line_index, position+1)]:
            if ((k,v) in allCoordinates):
                surrounding_coords.append(allCoordinates[(k,v)])
                if allCoordinates[(k,v)] != 9:
                    temp_surrounding_coords.append((k,v))

        if all(allCoordinates[(line_index, position)] < sc for sc in surrounding_coords):
            total_a += (allCoordinates[(line_index, position)] + 1)
            if (line_index, position) not in lowest_values:
                lowest_values[(line_index, position)] = []
            lowest_values[(line_index, position)].extend(temp_surrounding_coords)
        if (line_index, position) not in all_adjacent_values:
            all_adjacent_values[(line_index, position)] = []
        all_adjacent_values[(line_index, position)].extend(temp_surrounding_coords)

print("Total Part A:", total_a)

# Part B
for lowest_coordinate in lowest_values:
    for coordinate in lowest_values[lowest_coordinate]:
        for adj_coordinate in all_adjacent_values[coordinate]:
            if (adj_coordinate != lowest_coordinate) and (adj_coordinate not in lowest_values[lowest_coordinate]):
                lowest_values[lowest_coordinate].append(adj_coordinate)

final_values = []

for lv in lowest_values:
    final_values.append(len(lowest_values[lv])+1)

final_values.sort()
total_b = final_values[-1] * final_values[-2] * final_values[-3]

print('Total Part B:', total_b)
