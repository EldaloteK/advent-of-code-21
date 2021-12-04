#!/usr/bin/env python3

with open("../input/3ab.txt", "r") as report:
    report_numbers = [r.strip() for r in report.readlines()]

# # Part A
counters = []
final_gamma_rate = ""
final_epsilon_rate = ""

for i, num in enumerate(report_numbers[0]):
    counters.append({})

for i, num in enumerate(report_numbers):
    for k, ind_num in enumerate(num):
        if len(counters) and ind_num not in counters[k]:
            counters[k][ind_num] = 0
        counters[k][ind_num] += 1

for group in counters:
    final_gamma_rate += min(group, key=lambda k: group[k])
    final_epsilon_rate += max(group, key=lambda k: group[k])

print((int(final_gamma_rate, 2)) * (int(final_epsilon_rate, 2)))

# Part B
final = ""

def calculate_generator(nums, final, is_max):
    if len(final) == 12 or len(nums) == 1:
        return final
    else:
        counters2 = {}

        for i, num in enumerate(nums):
            if num[len(final)] not in counters2:
                counters2[num[len(final)]] = 0

            counters2[num[len(final)]] += 1

        if is_max:
            counters2_asc_sorted = dict(sorted(counters2.items(), reverse=True, key=lambda item: item[0]))

            final += max(counters2_asc_sorted, key=lambda k: counters2_asc_sorted[k])
        else:
            counters2_desc_sorted = dict(sorted(counters2.items(), key=lambda item: item[0]))

            final += min(counters2_desc_sorted, key=lambda k: counters2_desc_sorted[k])

        temp_li = list(filter((lambda x: str(x)[len(final) - 1] == final[len(final) - 1]), nums))

        if (len(temp_li)) == 1 and len(final) != 12:
            final += temp_li[0][len(final) : 12]

        return calculate_generator(temp_li, final, is_max)


o2_generator = calculate_generator(report_numbers, final, True)

co2_scrubber = calculate_generator(report_numbers, final, False)

print((int(o2_generator, 2)) * (int(co2_scrubber, 2)))
