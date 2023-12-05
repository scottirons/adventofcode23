# oh lawd
# boundary conds, difference factor something something idk
# ok store tuples in a list but also store tuple:subtraction factor key:values in a dictionary and trust the
# test input isn't fucking with me about continuity?

import re
import math
from collections import defaultdict


def day5a():

    convert_lists = []
    convert_factors = []
    with open('test.txt', 'r') as f:
        sections = f.read().split('\n\n')
        seeds = re.findall(r'\d+', sections[0])
        for section in sections[1:]:        # yea yea janky extra slicing i dont currr
            all_inputs = re.findall(r'\d+', section)
            curr_conversion = []
            curr_conversion_dict = defaultdict(int)
            for i in range(0, len(all_inputs), 3):
                dest, start, length = int(all_inputs[i]), int(all_inputs[i + 1]), int(all_inputs[i + 2])
                curr_conversion.append((start, start + length - 1))
                curr_conversion_dict[(start, start + length - 1)] = dest - start
            convert_lists.append(sorted(curr_conversion))
            convert_factors.append(curr_conversion_dict)
    print(convert_lists)

    curr_min = math.inf
    # now, for each shenanigan seed number lalalala check all the contiguous ranges then once
    # I find the matcher do the thing right
    for seed in seeds:
        curr_val = int(seed)
        for i, conversion in enumerate(convert_lists):
            for rng in conversion:
                if rng[0] <= curr_val <= rng[1]:
                    curr_val = curr_val + convert_factors[i][rng]
                    break
        curr_min = min(curr_min, curr_val)

    print(curr_min)


day5a()
