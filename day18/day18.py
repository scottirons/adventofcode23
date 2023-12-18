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
            self.ins.append((i[0], int(i[1])))
            self.ins_b.append((self.dir_key[c[-1]], int(c[1:-1], 16)))
        self.b_a = [(0, 0)]
        self.b_b = [(0, 0)]
        self.dirs = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1)
        }

    def solve(self, part_b=False):
        # fill out the border
        source = self.ins_b if part_b else self.ins
        dest = self.b_b if part_b else self.b_a
        points = 1
        curr_point = (0, 0)
        for ins in source:
            curr_point = (curr_point[0] + (self.dirs[ins[0]][0] * ins[1]), curr_point[1] + (self.dirs[ins[0]][1] * ins[1]))
            points += ins[1]
            dest.append(curr_point)

        sum_a = 0
        sum_b = 0
        for i in range(len(dest) - 1):
            sum_a += (dest[i][0] * dest[i + 1][1])
            sum_b += (dest[i][1] * dest[i + 1][0])
        total = abs(sum_a - sum_b) / 2

        # ok this was just pure guesswork (since we're already counting them in some capacity I just played around with
        # how to adjust the points add part until the test input worked
        return int(total + ((points + 1) // 2))


start = time.perf_counter()
sol = Solution("input.txt")
print(f'Part 1: {sol.solve()}')
print(f'Part 2: {sol.solve(True)}')
print(f'This all took {round(time.perf_counter() - start, 4)} seconds')
