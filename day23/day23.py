from collections import defaultdict
import time

DIRS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
)

HILLS = {
    '>': 0,
    '<': 1,
    'v': 2,
    '^': 3
}


def is_valid(val, m_r, m_c):
    return 0 <= val[0] <= m_r and 0 <= val[1] <= m_c


def solve(source):
    with open(source, 'r') as f:
        lines = f.read().split('\n')
    m_r, m_c = len(lines) - 1, len(lines[0]) - 1
    finish = (m_r, m_c - 1)
    curr_max = 0

    stack = [((0, 1), {(0, 1)})]
    while stack:
        curr_point, curr_set = stack.pop()
        for rm, cm in DIRS:
            r, c = curr_point[0] + rm, curr_point[1] + cm
            if (r, c) == finish:
                curr_max = max(curr_max, len(curr_set))
            elif is_valid((r, c), m_r, m_c) and (r, c) not in curr_set:
                c_set = set(curr_set)
                pt = lines[r][c]
                if pt == '.':
                    c_set.add((r, c))
                    stack.append(((r, c), set(c_set)))
                else:
                    while pt in '><v^':
                        c_set.add((r, c))
                        rr, cc = DIRS[HILLS[pt]]
                        r, c = r + rr, c + cc
                        if is_valid((r, c), m_r, m_c) and (r, c) not in c_set:
                            pt = lines[r][c]
                        else:
                            break
                    if pt == '.':
                        c_set.add((r, c))
                        stack.append(((r, c), set(c_set)))
    print(f'Part 1: {curr_max}')


def two_edges(point, graph):
    total = 0
    for r, c in DIRS:
        rr, cc = point[0] + r, point[1] + c
        if graph[rr][cc] in '.v>':
            total += 1
    return total == 2


def solve_b(source):
    with open(source, 'r') as f:
        lines = f.read().split('\n')
    m_r, m_c = len(lines) - 1, len(lines[0]) - 1
    start = (0, 1)
    finish = (m_r, m_c - 1)
    curr_max = 0

    # simplify graph
    checked = set()
    adj = defaultdict(dict)

    def condense(point):
        s = point
        checked.add(point)
        for a, b in DIRS:
            total = 0
            aa, bb = s[0] + a, s[1] + b
            if (aa, bb) not in checked and lines[aa][bb] in '>v.':
                while (aa, bb) not in {start, finish} and two_edges((aa, bb), lines):
                    total += 1
                    point = (aa, bb)
                    checked.add(point)
                    for aaa, bbb in DIRS:
                        aa, bb = aaa + point[0], bbb + point[1]
                        if (aa, bb) not in checked and lines[aa][bb] in '>v.':
                            break
                adj[s][(aa, bb)] = total + 1
                adj[(aa, bb)][s] = total + 1

    for r in range(1, len(lines) - 1):
        for c in range(1, len(lines[0]) - 1):
            if lines[r][c] in '.>v' and not two_edges((r, c), lines) and (r, c) not in checked:
                condense((r, c))

    stack = [((0, 1), {(0, 1)}, 0)]
    while stack:
        curr_point, curr_set, curr_len = stack.pop()
        for path in adj[curr_point]:
            c_len = curr_len
            c_set = set(curr_set)
            if path not in c_set:
                c_len += adj[curr_point][path]
            if path == finish:
                curr_max = max(curr_max, c_len)
            elif path not in c_set:
                c_set.add(path)
                stack.append((path, c_set, c_len))

    print(f'Part 2: {curr_max}')


start_a = time.perf_counter()
solve('input.txt')
print(f'Part 1 took {round(time.perf_counter() - start_a, 4)} seconds')
start_b = time.perf_counter()
solve_b('input.txt')
print(f'Part 2 took {round(time.perf_counter() - start_b, 4)} seconds lol')
