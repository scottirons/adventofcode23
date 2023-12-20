import time
from math import prod
from collections import defaultdict
INDEX_KEY = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3
}


def pass_cond(cond, part):
    if len(cond) == 1:
        return True
    if cond[1] == '<':
        return part[cond[0]] < cond[2]
    return part[cond[0]] > cond[2]


def solve_a(wf, parts):
    a = []
    for p in parts:
        curr_key = 'in'
        while curr_key not in 'RA':             # USA USA USA RAAAAAAAAA
            ins = wf[curr_key]
            valid = False
            i = 0
            while not valid:
                curr_ins = ins[i]
                if pass_cond(curr_ins, p):
                    valid = True
                    curr_key = curr_ins[-1]
                i += 1
        if curr_key == 'A':
            a.append(p)
    return sum(sum(p) for p in a)


def solve_b(wf, part_range, curr_key):

    # base cases
    if curr_key == 'A':
        return prod((b - a + 1) for a, b in part_range)
    elif curr_key == 'R':
        return 0

    total = 0
    for flow in wf[curr_key]:
        # non-conditional branch
        if len(flow) == 1:
            total += solve_b(wf, part_range, flow[-1])
        # dang can't really use my pass_cond() function lol
        elif flow[1] == '<':
            # there's some validity to be had
            if part_range[flow[0]][0] < flow[2]:
                new_ranges = list(part_range)
                new_range = (part_range[flow[0]][0], min(part_range[flow[0]][1], flow[2] - 1))
                new_ranges[flow[0]] = new_range
                total += solve_b(wf, new_ranges, flow[-1])
                # no ability to keep going in the "it's not less than this number" case
                if flow[2] > part_range[flow[0]][1]:
                    break
                part_range[flow[0]] = (flow[2], part_range[flow[0]][1])
        elif flow[1] == '>':
            if part_range[flow[0]][1] > flow[2]:
                new_ranges = list(part_range)
                new_range = (max(part_range[flow[0]][0], flow[2] + 1), part_range[flow[0]][1])
                new_ranges[flow[0]] = new_range
                total += solve_b(wf, new_ranges, flow[-1])
                if flow[2] < part_range[flow[0]][0]:
                    break
                part_range[flow[0]] = (part_range[flow[0]][0], flow[2])
    return total

def main(source):
    wf_dict = defaultdict(list)
    parts_list = []
    with open(source, 'r') as f:
        lines = f.read().split('\n\n')
    wf = lines[0].split('\n')
    parts = lines[1].split('\n')
    for f in wf:
        key, rest = f[:-1].split('{')
        ins = rest.split(',')
        for i in ins:
            if ':' in i:
                op, dest = i.split(':')
                k = INDEX_KEY[op[0]]
                o = op[1]
                n = int(op[2:])
                wf_dict[key].append((k, o, n, dest))
            else:
                wf_dict[key].append((i,))
    for part in parts:
        p = part[1:-1].split(',')
        curr_parts = []
        for i in p:
            curr_parts.append(int(i[2:]))
        parts_list.append(curr_parts)

    start = time.perf_counter()
    print(f'Part 1: {solve_a(wf_dict, parts_list)}, which took {round(time.perf_counter() - start, 4)} seconds')

    start_2 = time.perf_counter()
    print(f'Part 2: {solve_b(wf_dict, [(1, 4000), (1, 4000), (1, 4000), (1, 40000)], "in")}, which took {round(time.perf_counter() - start_2, 4)} seconds')


if __name__ == "__main__":
    main('input.txt')
