import re
import math


def day8a():
    with open('input.txt', 'r') as f:
        sections = f.read().split('\n\n')
    dirs = sections[0]
    maps = sections[1].split('\n')
    paths = {}
    for m in maps:
        pieces = re.findall(r'\w+', m)
        paths[pieces[0]] = (pieces[1], pieces[2])

    count = 0
    curr_nodes = [key for key in paths if key[2] == 'A']
    first_end = [0 for _ in curr_nodes]

    while True:
        next_step = dirs[count % len(dirs)]
        if next_step == 'R':
            for i, node in enumerate(curr_nodes):
                curr_nodes[i] = paths[node][1]
        else:
            for i, node in enumerate(curr_nodes):
                curr_nodes[i] = paths[node][0]

        count += 1
        num_end = 0
        for i, node in enumerate(curr_nodes):
            if node[2] == 'Z':
                num_end += 1
                if not first_end[i]:
                    first_end[i] = count
        if 0 not in first_end:
            break

    return math.lcm(first_end[0], first_end[1], first_end[2], first_end[3], first_end[4], first_end[5])


print(f'Part 2: {day8a()}')
