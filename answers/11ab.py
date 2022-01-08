#!/usr/bin/env python3

with open("../input/11ab.txt", "r") as report:
    initial_lines = [[int(k.strip()) for k in r.strip()] for r in report.readlines()]

board_length = len(initial_lines[0])

all_coordinates = {(i, c):initial_lines[i][c] for i in range(len(initial_lines)) for c in range(board_length)}

flash_count = 0
all_adjacent_octos = {}

for li_ind, line in enumerate(initial_lines):
        for pos in range(board_length):
            surrounding_coords = []
            for (k,v) in [(li_ind-1, pos), (li_ind+1, pos), (li_ind, pos-1), (li_ind, pos+1)]:
                if ((k,v) in all_coordinates):
                    surrounding_coords.append((k,v))

            for (dk1, dv1) in [(li_ind-1, pos-1), (li_ind+1, pos-1), (li_ind-1, pos+1), (li_ind+1, pos+1)]:
                if ((dk1,dv1) in all_coordinates):
                    surrounding_coords.append((dk1,dv1))
            if (li_ind, pos) not in all_adjacent_octos:
                all_adjacent_octos[(li_ind, pos)] = []
            all_adjacent_octos[(li_ind, pos)].extend(surrounding_coords)

# Part A and B
steps = 0
while(True):
    steps += 1
    # Contains all octos that have flashed.
    flash_library = {}

    # Contains initial octos and their corresponding adjacent octos.
    temp_octo_dict = {}

    # Increase all octo levels by 1
    for line_index, line in enumerate(initial_lines):
        for position in range(board_length):
            all_coordinates[(line_index,position)] += 1
            if (line_index, position) not in temp_octo_dict:
                temp_octo_dict[(line_index, position)] = []
            temp_octo_dict[(line_index, position)].extend(all_adjacent_octos[(line_index, position)])

    for octo in temp_octo_dict:
        if all_coordinates[octo] > 9 and octo not in flash_library:
            flash_count += 1
            flash_library[(octo)] = 0
            for adj_octo in temp_octo_dict[octo]:
                all_coordinates[adj_octo] += 1
                if all_coordinates[adj_octo] > 9 and adj_octo not in flash_library:
                    flash_count += 1
                    flash_library[(adj_octo)] = 0
                    temp_octo_dict[octo].extend(all_adjacent_octos[adj_octo])

    for octo_that_flashed in flash_library:
        all_coordinates[octo_that_flashed] = 0

    if len(flash_library) == len(all_coordinates):
        break

    if steps == 100:
        print("Part A flash fount: ", flash_count)

print("Part B steps: ", steps)
