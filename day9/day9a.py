import re


class Solution:
    def __init__(self):
        self.lines = None
        self.num_lines = None
        self.next_num_sum = 0

    def parse(self):
        with open('input.txt', 'r') as f:
            self.lines = f.read().split('\n')

        self.num_lines = [[int(val) for val in re.findall(r'-*\d+', line)] for line in self.lines]

    def solve_a(self):
        for line in self.num_lines:
            self.next_num_sum += (self.find_next_num(line) + line[-1])

    def find_next_num(self, seq):
        next_seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        if all(num == 0 for num in next_seq):
            return 0
        return next_seq[-1] + self.find_next_num(next_seq)


sol = Solution()
sol.parse()
sol.solve_a()
print(sol.next_num_sum)
