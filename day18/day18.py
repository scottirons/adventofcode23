import re
import time


class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            ins = f.read().split('\n')
        self.ins = []
        self.ins_b = []
        self.dir_key = {
            "0": "R",
            "1": "D",
            "2": "L",
            "3": "U"
        }
        for i in ins:
            i = i.split(' ')
            c = i[2][1:-1]
            self.ins.append((i[0], int(i[1]), c))
            self.ins_b.append((self.dir_key[c[-1]], int(c[1:-1], 16)))
        print(self.ins_b)
        self.b_a = [(0, 0)]
        self.dir_a = [self.ins[0][0]]
        self.i_a = set()
        self.dirs = {
            "R": (0, 1),
            "L": (0, -1),
            "U": (-1, 0),
            "D": (1, 0)
        }
        self.shift = {
            "R": "D",
            "L": "U",
            "U": "R",
            "D": "L"
        }

    def solve(self):
        # fill out the border
        curr_point = (0, 0)
        for ins in self.ins:
            for _ in range(ins[1]):
                curr_point = (curr_point[0] + self.dirs[ins[0]][0], curr_point[1] + self.dirs[ins[0]][1])
                self.b_a.append(curr_point)
                self.dir_a.append(ins[0])

        # test is enclosed to the right, not sure about input
        for i, (x, y) in enumerate(self.b_a):
            (a, b) = self.dirs[self.shift[self.dir_a[i]]]
            p = (a + x, b + y)
            while p not in self.b_a:
                self.i_a.add(p)
                p = (p[0] + a, p[1] + b)
        return len(self.i_a) + len(self.b_a)


start = time.perf_counter()
sol = Solution("test.txt")
print(f"Part A: {sol.solve()}, which took {round(time.perf_counter() - start, 4)} seconds")
