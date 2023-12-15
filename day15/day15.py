class Solution:
    def __init__(self, source):
        with open(source, "r") as f:
            self.seq = f.read().split(',')

    @staticmethod
    def parse_line(line):
        result = 0
        for c in line:
            result += ord(c)
            result *= 17
            result = result % 256
        return result

    def solve(self, part_b=False):
        if not part_b:
            return sum(self.parse_line(line) for line in self.seq)
        buckets = {i: [] for i in range(256)}
        nums = {i: {} for i in range(256)}
        for line in self.seq:
            if '-' in line:
                split_line = line.split('-')
                key = self.parse_line(split_line[0])
                if split_line[0] in buckets[key]:
                    buckets[key].remove(split_line[0])
                    del nums[key][split_line[0]]
            else:
                split_line = line.split('=')
                key = self.parse_line(split_line[0])
                if split_line[0] not in nums[key]:
                    buckets[key].append(split_line[0])
                nums[key][split_line[0]] = int(split_line[1])
        total = 0
        for i in buckets:
            for j, key in enumerate(buckets[i]):
                total += ((i + 1) * (j + 1) * nums[i][key])
        return total


sol = Solution("input.txt")
print(sol.solve())
print(sol.solve(True))
