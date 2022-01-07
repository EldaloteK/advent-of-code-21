#!/usr/bin/env python3

with open("../input/8ab.txt", "r") as report:
    initial_lines = [r.strip() for r in report.readlines()]

signal_patterns = []
output = []

for line in initial_lines:
    line_divided = line.split(' | ')
    l1 = line_divided[0].split()
    l2 = line_divided[1].split()
    signal_patterns.append(l1)
    output.append(l2)

"""
corr_nums: dictionary with keys as placement of lights:
    light 4 example:
        ....
       1    2
       1    2
        3333
       .    5
       .    5
        ....
"""
corr_nums = {
    (0,1,2,4,5,6): 0,
    (2,5): 1,
    (0,2,3,4,6): 2,
    (0,2,3,5,6): 3,
    (1,2,3,5): 4,
    (0,1,3,5,6): 5,
    (0,1,3,4,5,6): 6,
    (0,2,5): 7,
    (0,1,2,3,4,5,6): 8,
    (0,1,2,3,5,6): 9
}

# Base lights
lights = {
    2: {
        'corr_num': 1,
        'pattern': ['x','x','','x','x','','x'],
        'pattern_places': [2,5]
    },
    4: {
        'corr_num': 4,
        'pattern': ['x','','','','x','','x'],
        'pattern_places': [1,2,3,5]
    },
    3: {
        'corr_num': 7,
        'pattern': ['','x','','x','x','','x'],
        'pattern_places': [0,2,5]
    },
    7: {
        'corr_num': 8,
        'pattern': ['','','','','','',''],
        'pattern_places': [0,1,2,3,4,5,6]
    }
}


# Part A
count = 0
for i in output:
    for k in i:
        if len(k) in lights:
            count += 1
print("Part A total: ", count)

# Part B
final_total = 0

for index_j, j in enumerate(signal_patterns):
    lengths = {}
    final_pattern = ['x','x','x','x','x','x','x']
    sorted_signal_patterns = j
    sorted_signal_patterns.sort(key=lambda item: (+len(item), item))

    for ind_pattern in sorted_signal_patterns:
        if len(ind_pattern) not in lengths:
            lengths[len(ind_pattern)] = []
        lengths[len(ind_pattern)].append(ind_pattern)

    # What does length: 3 have that length: 2 does not?
    if len(lengths[2]) > 0:
        length_2 = set(lengths[2][0])
        if len(lengths[3]) > 0:
            length_3 = set(lengths[3][0])
            diff32 = list(length_3 - length_2)
            final_pattern[0] = diff32[0]
            two_leftover = list(length_3 - set(diff32[0]))
    # What two items does length: 4 have that length: 2 does not?
    if len(lengths[4]) > 0:
        length_4 = set(lengths[4][0])
        diff42 = list(length_4 - length_2)
    # Find a length: 6 that doesn't have both two_leftover.
    if len(lengths[6]) > 0:
            for len6 in lengths[6]:
                if ((two_leftover[0] and not two_leftover[1] in len6) or (not two_leftover[0] and two_leftover[1] in len6) or two_leftover[1] and not two_leftover[0] in len6) or (not two_leftover[1] and two_leftover[0] in len6):
                    two_leftover_item = [k for k in len6 if k == two_leftover[0] or k  == two_leftover[1]]
                    final_pattern[5] = two_leftover_item[0]
                    two_leftover_item2 = list(set(two_leftover_item).symmetric_difference(set([two_leftover[0], two_leftover[1]])))
                    final_pattern[2] = two_leftover_item2[0]
                    break
    # Find a length: 5 that only has final_pattern[5] and not final_pattern[2].
    if len(lengths[5]) > 0:
        for len5e in lengths[5]:
            if (final_pattern[5] and not final_pattern[2] in len5e):
                len5_with_fp5 = len5e
                break
        if len5_with_fp5:
            # Find a length: 5 that only has both E and B.
            for len5be in lengths[5]:
                if (final_pattern[5] in len5be and final_pattern[2] in len5be):
                    diff_5be = list(set(len5_with_fp5) - set(len5be))
                    final_pattern[1] = diff_5be[0]
                    k = list(set(diff42) - set(final_pattern[1]))
                    final_pattern[3] = k[0]
                    break
    # What does length: 7 have that is not in len5_with_fp5 that is not final_pattern[2]
    if len(lengths[7]) > 0:
        diff_85 = list(set(lengths[7][0]) - set(len5_with_fp5))
        diff_852 = list(set(diff_85) - set(final_pattern[2]))
        final_pattern[4] = diff_852[0]
        # What does length: 7 have that is not in final pattern?
        final_diff = list(set(lengths[7][0]) - set(final_pattern))
        final_pattern[6] = final_diff[0]

    sub_total_str = ""
    for output_item in output[index_j]:
        fi_li = list(final_pattern.index(k) for k in output_item)
        fi_li.sort()
        sub_total_str += str(corr_nums[tuple(fi_li)])
    final_total += int(sub_total_str)
print("Part B total: ", final_total)
