from sympy import symbols, Eq
from sympy import solve as solve_s


def right_dir(start, slope, val):
    if slope <= 0:
        return val <= start
    return val > start


def same_line_intersect(m, b, rng):
    low, high = rng
    xl = (low - b) / m
    xh = (high - b) / m
    yl = m * low + b
    yh = m * high + b
    poss = []
    if low <= xl <= high:
        poss.append((xl, low))
    if low <= xh <= high:
        poss.append((xh, high))
    if low <= yl <= high:
        poss.append((low, yl))
    if low <= yh <= high:
        poss.append((high, yh))
    return poss


def intersect(a, b, rng, pt_b=False):
    m1, b1 = a
    m2, b2 = b
    low, high = rng
    if m1 == m2:
        return same_line_intersect(m1, b1, rng) if b1 == b2 else []
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    if not pt_b:
        return [(x, y)] if low <= x <= high and low <= y <= high else []
    return [(x, y)]


def conv_mx_b(x, y, dx, dy):
    b = -((dy / dx) * x - y)
    return dy / dx, b


def parse_input(source):
    xyz = []
    mx_b = []
    with open(source, 'r') as f:
        lines = f.read().split('\n')
    for line in lines:
        pts, move = line.split(' @ ')
        pts = [int(pt) for pt in pts.split(', ')]
        mvs = [int(mv) for mv in move.split(', ')]
        xyz.append((tuple(pts), tuple(mvs)))
        mx_b.append(conv_mx_b(pts[0], pts[1], mvs[0], mvs[1]))
    return xyz, mx_b


def solve(source, low, high):
    xyz, mx_b = parse_input(source)

    # part 1
    total = 0
    for i in range(len(mx_b)):
        for j in range(i + 1, len(mx_b)):
            pts = intersect(mx_b[i], mx_b[j], (low, high))
            add = 0
            for pt in pts:
                if right_dir(xyz[i][0][0], xyz[i][1][0], pt[0]) and right_dir(xyz[i][0][1], xyz[i][1][1], pt[1]) and \
                        right_dir(xyz[j][0][0], xyz[j][1][0], pt[0]) and right_dir(xyz[j][0][1], xyz[j][1][1], pt[1]):
                    add = 1
            total += add

    # part 2 gotta just solve a bunch of 'y = mx + b' equations but for each dimension
    # ok Sympy seems to do the trick
    a, b, c = xyz[0], xyz[1], xyz[2]
    x, y, z, dx, dy, dz, t1, t2, t3 = symbols('x y z dx dy dz t1 t2 t3')
    eq1 = Eq(x + dx * t1, a[0][0] + a[1][0] * t1)
    eq2 = Eq(y + dy * t1, a[0][1] + a[1][1] * t1)
    eq3 = Eq(z + dz * t1, a[0][2] + a[1][2] * t1)
    eq4 = Eq(x + dx * t2, b[0][0] + b[1][0] * t2)
    eq5 = Eq(y + dy * t2, b[0][1] + b[1][1] * t2)
    eq6 = Eq(z + dz * t2, b[0][2] + b[1][2] * t2)
    eq7 = Eq(x + dx * t3, c[0][0] + c[1][0] * t3)
    eq8 = Eq(y + dy * t3, c[0][1] + c[1][1] * t3)
    eq9 = Eq(z + dz * t3, c[0][2] + c[1][2] * t3)
    sol = solve_s([eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9], (x, y, z, dx, dy, dz, t1, t2, t3))
    r = sol[0]

    return total, r[0] + r[1] + r[2]


def main(source):
    lo, high = 200000000000000, 400000000000000
    if source == 'test.txt':
        lo, high = 7, 27
    sol = solve(source, lo, high)
    print(f'Part 1: {sol[0]}')
    print(f'Part 2: {sol[1]}')


if __name__ == "__main__":
    main('input.txt')
