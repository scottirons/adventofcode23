from collections import defaultdict


def find_min_max(brick):
    z1, y1, x1, z2, y2, x2 = brick[0][0], brick[0][1], brick[0][2], brick[1][0], brick[1][1], brick[1][2]
    min_z, max_z = min(z1, z2), max(z1, z2) + 1
    min_y, max_y = min(y1, y2), max(y1, y2) + 1
    min_x, max_x = min(x1, x2), max(x1, x2) + 1
    return min_z, max_z, min_y, max_y, min_x, max_x


def solve(source):
    with open(source, 'r') as f:
        lines = f.read().split('\n')
    bricks = []
    r_o = defaultdict(list[tuple])   # blocks a particular one is resting on
    r_a = defaultdict(list[tuple])   # blocks resting on top (above)
    min_max = defaultdict()
    sq_m = defaultdict(tuple)        # matching particular squares to particular blocks
    for line in lines:
        first, second = [int(i) for i in line.split('~')[0].split(',')], [int(i) for i in line.split('~')[1].split(',')]
        brick = tuple(sorted((tuple(reversed(first)), tuple(reversed(second)))))

        # figure out which blocks correspond to which bricks
        min_max[brick] = (find_min_max(brick))
        bricks.append(brick)

    for brick in sorted(bricks):
        # just manually do the first one idk...
        if not sq_m:
            dif = brick[0][0] - 1
            new_brick = ((brick[0][0] - dif, brick[0][1], brick[0][2]), (brick[1][0] - dif, brick[1][1], brick[1][2]))
            min_z, max_z, min_y, max_y, min_x, max_x = find_min_max(new_brick)
            for z in range(min_z, max_z):
                for y in range(min_y, max_y):
                    for x in range(min_x, max_x):
                        sq_m[(z, y, x)] = new_brick

        min_z, max_z, min_y, max_y, min_x, max_x = min_max[brick]
        # starting at min_z, go down from each block at that level until I hit 1 or another block, keep track of the
        # HIGHEST block I run into
        hit = defaultdict(set)
        for z in range(min_z, 0, -1):
            for y in range(min_y, max_y):
                for x in range(min_x, max_x):
                    if (z - 1, y, x) in sq_m:
                        hit[z].add(sq_m[(z - 1, y, x)])
        m_h = max(hit) if hit else 1
        dif = brick[0][0] - m_h
        new_brick = ((brick[0][0] - dif, brick[0][1], brick[0][2]), (brick[1][0] - dif, brick[1][1], brick[1][2]))
        min_z, max_z, min_y, max_y, min_x, max_x = find_min_max(new_brick)
        for z in range(min_z, max_z):
            for y in range(min_y, max_y):
                for x in range(min_x, max_x):
                    sq_m[(z, y, x)] = new_brick
        h = hit[max(hit)] if hit else []
        for b in h:
            r_o[new_brick].append(b)
            r_a[b].append(new_brick)

    # part a
    total = len(bricks) - len(r_a)
    for b in r_a:
        add = True
        for br in r_a[b]:
            add = len(r_o[br]) > 1 and add
        total += 1 if add else False
    print(total)




solve("test.txt")
