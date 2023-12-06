import re
import math
from collections import defaultdict
import time


def day5b():

    convert_lists = []
    convert_factors = []
    process_stacc = []
    curr_min = math.inf

    with open('input.txt', 'r') as f:
        sections = f.read().split('\n\n')

    seeds = re.findall(r'\d+', sections[0])
    for section in sections[1:]:
        all_inputs = re.findall(r'\d+', section)
        curr_conversion = []
        curr_conversion_dict = defaultdict(int)
        for i in range(0, len(all_inputs), 3):
            dest, start, length = int(all_inputs[i]), int(all_inputs[i + 1]), int(all_inputs[i + 2])
            curr_conversion.append((start, start + length - 1))
            curr_conversion_dict[(start, start + length - 1)] = dest - start
        convert_lists.append(sorted(curr_conversion))
        convert_factors.append(curr_conversion_dict)

    def process_range(rng_val):
        nonlocal curr_min                       # u can't tell me what to do, scoping
        #print(f'processing: {rng_val}')

        # curr_stack value is a final "we can reach this range" range
        if rng_val[0] == len(convert_lists):
            curr_min = min(rng_val[1][0], curr_min)
            return
        cur_min, cur_max = rng_val[1][0], rng_val[1][1]
        rng_i = rng_val[0]
        ranges = convert_lists[rng_i]
        if cur_min < ranges[0][0]:
            next_min = min(cur_max, ranges[0][1])
            process_stacc.append((rng_i + 1, (cur_min, next_min)))
            if next_min == cur_max:
                return
            cur_min = next_min + 1
        for rnge in ranges:
            if cur_min <= rnge[1]:
                next_min = min(cur_max, rnge[1])
                process_stacc.append((rng_i + 1, (cur_min + convert_factors[rng_i][rnge],
                                                  next_min + convert_factors[rng_i][rnge])))
                if next_min == cur_max:
                    return
                cur_min = next_min + 1
        if cur_min <= cur_max:
            process_stacc.append((rng_i + 1, (cur_min, cur_max)))

    for j in range(0, len(seeds), 2):
        start, end = int(seeds[j]), int(seeds[j]) + int(seeds[j + 1]) - 1
        process_stacc.append((0, (start, end)))
        while process_stacc:
            process_range(process_stacc.pop())

    return curr_min


strt = time.perf_counter()
print(f'Day 5 part b solution: {day5b()}')
print(f'This took {time.perf_counter() - strt} seconds')
