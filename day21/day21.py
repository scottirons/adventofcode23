DIRS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
)


def part_1(source):
    start = (0, 0)
    with open(source, 'r') as f:
        lines = f.read().split('\n')
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                start = (i, j)
                lines[i] = lines[i].replace('S', '.')
    max_r, max_c = len(lines) - 1, len(lines[0]) - 1

    process = [start]
    for _ in range(64):
        visited = set()
        next_process = []
        for coord in process:
            for d in DIRS:
                next_c = (coord[0] + d[0], coord[1] + d[1])
                if 0 <= next_c[0] <= max_r and 0 <= next_c[1] <= max_c and next_c not in visited and \
                        lines[next_c[0]][next_c[1]] == '.':
                    visited.add(next_c)
                    next_process.append(next_c)
        process = next_process
    print(len(process))


def part_2(source):
    start = (0, 0)
    with open(source, 'r') as f:
        lines = f.read().split('\n')
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                start = (i, j)
                lines[i] = lines[i].replace('S', '.')
    max_r, max_c = len(lines) - 1, len(lines[0]) - 1

    process = [start]
    for i in range(1, 65 + (131 * 2) + 1):
        visited = set()
        next_process = []
        for rr, cc in process:
            for r, c in DIRS:
                next_r, next_c = rr + r, cc + c
                next_rr, next_cr = next_r % len(lines), next_c % len(lines[0])
                if 0 <= next_rr <= max_r and 0 <= next_cr <= max_c and (next_r, next_c) not in visited and \
                        lines[next_rr][next_cr] == '.':
                    visited.add((next_r, next_c))
                    next_process.append((next_r, next_c))
        process = next_process
        if i in {65, 65 + 131}:
            print(len(process))
    print(len(process))
    print(15085 * (26501365//131) * (26501365//131) + 15195 * (26501365//131) + 3819)


if __name__ == "__main__":
    part_2('input.txt')
