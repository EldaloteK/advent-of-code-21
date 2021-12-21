#!/usr/bin/env python3

with open("../input/6ab.txt", "r") as report:
    initial_ages = [r.strip().split(',') for r in report.readlines()]

def lantern_fish_calculation(days):
    ages = []
    lantern_fish_counts = {}

    for k in range(9):
        lantern_fish_counts[k] = 0

    for age in initial_ages[0]:
        age_num = int(age)
        ages.append(age_num)
        lantern_fish_counts[age_num] += 1

    for day in range(days):
        if (lantern_fish_counts[0] > 0):
            temp_zero_count = lantern_fish_counts[0]
            lantern_fish_counts[0] = 0

            for fish_stage, fish_count in  lantern_fish_counts.items():
                if ((fish_stage != 0) and fish_count > 0):
                    lantern_fish_counts[fish_stage - 1] = lantern_fish_counts[fish_stage]
                    lantern_fish_counts[fish_stage] = 0

            lantern_fish_counts[8] += temp_zero_count
            lantern_fish_counts[6] += temp_zero_count

        else:
            for fish_stage, fish_count in  lantern_fish_counts.items():
                if (fish_count > 0):
                    lantern_fish_counts[fish_stage - 1] = lantern_fish_counts[fish_stage]
                    lantern_fish_counts[fish_stage] = 0
    print('After', days, 'days:', sum(lantern_fish_counts.values()))

lantern_fish_calculation(80)
lantern_fish_calculation(256)

