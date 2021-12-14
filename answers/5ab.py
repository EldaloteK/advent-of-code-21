#!/usr/bin/env python3
import re

with open("../input/5ab.txt", "r") as report:
    ranges = [r.strip() for r in report.readlines()]

temp = []
coord_dict = {}

for r in ranges:
    range_match = re.match(r"(\d+,\d+) -> (\d+,\d+)", r)
    temp.append(range_match.groups())

for t in temp:
    # Part A
    start = t[0]
    end = t[1]
    start_x, start_y = map(int, start.split(','))
    end_x, end_y = map(int, end.split(','))

    if (abs(int(start_x)-int(end_x)) != abs(int(start_y)-int(end_y))):
        if (start_x == end_x):
            if (start_y > end_y):
                kl1 = [*range(end_y, start_y + 1)]
            else:
                kl1 = [*range(start_y, end_y+1)]

            for r in kl1:
                if (str(start_x) + ',' + str(r)) not in coord_dict:
                    coord_dict[(str(start_x) + ',' + str(r))] = 0
                else:
                    coord_dict[(str(start_x) + ',' + str(r))] = 1
        else:
            if (int(start_x) > int(end_x)):
                kl1 = [*range(end_x, start_x+1)]
            else:
                kl1 = [*range(start_x, end_x+1)]

            for r in kl1:
                if (str(r)+ ',' + str(start_y)) not in coord_dict:
                    coord_dict[(str(r)+ ',' + str(start_y))] = 0
                else:
                    coord_dict[(str(r)+ ',' + str(start_y))] = 1
    # Part B
    else:
        if (start_y > end_y):
            kb2 = [*range(start_y, end_y - 1, -1)]
        else:
            kb2 = [*range(start_y, end_y + 1)]

        if (start_x > end_x):
            kb3 = [*range(start_x, end_x - 1, -1)]
        else:
            kb3 = [*range(start_x, end_x + 1)]

        for index, r in enumerate(kb2):
            if (str(kb3[index])+ ',' + str(r)) not in coord_dict:
                coord_dict[(str(kb3[index]) + ',' + str(r))] = 0
            else:
                coord_dict[(str(kb3[index]) + ',' + str(r))] = 1

print(sum(coord_dict.values()))