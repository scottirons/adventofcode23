import re


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
    curr_node = 'AAA'
    while curr_node != 'ZZZ':
        next_step = dirs[count % len(dirs)]
        if next_step == 'R':
            curr_node = paths[curr_node][1]
        else:
            curr_node = paths[curr_node][0]
        count += 1

    return count


print(f'Part 1: {day8a()}')
