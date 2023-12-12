class Solution:
    def __init__(self, source):
        self.lines = []
        self.parse_input(source)
        self.memo = {}

    def parse_input(self, source):
        with open(source, "r") as f:
            lines = f.read().split('\n')
            for line in lines:
                self.lines.append(line.split())

    def is_valid(self, line, pattern):
        counts = []
        curr_count = 0
        for i, char in enumerate(line):
            if char == '#':
                curr_count += 1
                if i == len(line) - 1:
                    counts.append(curr_count)
            else:
                if curr_count:
                    counts.append(curr_count)
                curr_count = 0
        return counts == pattern

    def find_possibilities(self, line, pattern):
        result = 0
        possibilities = [line]
        i = 0
        while i < len(possibilities):
            curr_l = possibilities[i]
            line_a = list(curr_l)
            line_b = list(curr_l)
            for j, c in enumerate(curr_l):
                if c == '?':
                    line_a[j] = '.'
                    line_b[j] = '#'
                    possibilities.append(line_a)
                    possibilities.append(line_b)
                    break
            i += 1
        for l in possibilities:
            if self.is_valid(l, pattern) and '?' not in l:
                result += 1
        return result

    def solve_a(self):
        result = 0
        for line in self.lines:
            result += self.find_possibilities([c for c in line[0]], [int(c) for c in line[1].split(',')])
        return result

    def dp(self, line, nums, seq_i, num_i, curr_l, curr_seq):
        if (seq_i, num_i, curr_l) in self.memo:
            return self.memo[(seq_i, num_i, curr_l)]

        # base case
        if seq_i == len(line):
            # we've gone through numbers and aren't currently counting a sequence
            if num_i == len(nums) and curr_l == 0:
                return 1
            # we're at the final number and the current count == that number
            if num_i == len(nums) - 1 and curr_l == nums[num_i]:
                return 1
            return 0

        # try '.' and '#'
        total = 0
        c = line[seq_i]
        for target in '.#':
            if c == target or c == '?':
                if target == '.' and curr_l == 0:
                    total += self.dp(line, nums, seq_i + 1, num_i, 0, curr_seq + '.')
                elif target == '.' and curr_l > 0 and num_i < len(nums) and curr_l == nums[num_i]:
                    total += self.dp(line, nums, seq_i + 1, num_i + 1, 0, curr_seq + '.')
                elif target == '#':
                    total += self.dp(line, nums, seq_i + 1, num_i, curr_l + 1, curr_seq + '#')
        self.memo[(seq_i, num_i, curr_l)] = total
        return total

    # keep track of current index, which number we're on, length of sequence we're at
    def solve(self, b: bool):
        result = 0
        for line in self.lines:
            self.memo = {}
            if b:
                line[0] = line[0] + '?' + line[0] + '?' + line[0] + '?' + line[0] + '?' + line[0]
                line[1] = line[1] + ',' + line[1] + ',' + line[1] + ',' + line[1] + ',' + line[1]
            nums = [int(num) for num in line[1].split(',')]
            result += self.dp(line[0], nums, 0, 0, 0, line[0][0])
        return result


sol = Solution("input.txt")
print(sol.solve(False))
print(sol.solve(True))

