class Solution:
    def __init__(self, source):
        self.lines = []
        self.parse_input(source)

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
            print(f'processing: {line}')
            result += self.find_possibilities([c for c in line[0]], [int(c) for c in line[1].split(',')])
        return result


sol = Solution("input.txt")
print(sol.solve_a())

