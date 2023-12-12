class Solution:
    def __init__(self, source):
        self.thicc_rows = set()
        self.thicc_cols = set()
        self.expanded_grid = self.parse_input(source)

    def parse_input(self, source):
        with open(source, "r") as f:
            lines = f.read().split('\n')
        split_lines = [[char for char in line] for line in lines]
        # find chonky rows
        for i, row in enumerate(split_lines):
            if all(c == '.' for c in split_lines[i]):
                self.thicc_rows.add(i)

        # find chonky columns
        for j in range(len(split_lines[0])):
            add = True
            for i in range(len(split_lines)):
                if split_lines[i][j] != '.':
                    add = False
            if add:
                self.thicc_cols.add(j)

        return split_lines

    def solve(self, jump):
        galaxies = []
        for i in range(len(self.expanded_grid)):
            for j in range(len(self.expanded_grid[0])):
                if self.expanded_grid[i][j] == '#':
                    galaxies.append((i, j))
        total_distance = 0
        for i in range(len(galaxies)):
            for j in range(i, len(galaxies)):
                a, b = galaxies[i], galaxies[j]
                total_distance += (max(a[1], b[1]) - min(a[1], b[1]))
                for c in range(min(a[1], b[1]), max(a[1], b[1])):
                    if c in self.thicc_cols:
                        total_distance += jump
                total_distance += (max(a[0], b[0]) - min(a[0], b[0]))
                for r in range(min(a[0], b[0]), max(a[0], b[0])):
                    if r in self.thicc_rows:
                        total_distance += jump
        return total_distance


sol = Solution("input.txt")
print(f"Part A: {sol.solve(1)}")
print(f"Part B: {sol.solve(999999)}")
