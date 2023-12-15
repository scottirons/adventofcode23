from collections import deque, defaultdict
import time


class Solution:
    def __init__(self, source):
        self.grid = self.parse(source)

    @staticmethod
    def parse(source):
        with open(source, "r") as f:
            return [list(line) for line in f.read().split('\n')]

    def solve(self):
        total = 0
        num_rows = len(self.grid)
        num_cols = len(self.grid[-0])
        for c in range(num_cols):
            q = deque()
            for r in range(num_rows):
                next_point = self.grid[r][c]
                if next_point == '#':
                    q = deque()
                elif next_point == '.':
                    q.append((r, c))
                else:
                    if q:
                        opening = q.popleft()
                        self.grid[opening[0]][opening[1]] = 'O'
                        self.grid[r][c] = '.'
                        q.append((r, c))
        for r in range(num_rows):
            for c in range(num_cols):
                total += num_rows - r if self.grid[r][c] == 'O' else 0
        return total

    def solve_b(self):
        memo = defaultdict()
        num_rows = len(self.grid)
        num_cols = len(self.grid[-0])
        for i in range(1_000):
            total = 0
            # north
            for c in range(num_cols):
                q = deque()
                for r in range(num_rows):
                    next_point = self.grid[r][c]
                    if next_point == '#':
                        q = deque()
                    elif next_point == '.':
                        q.append((r, c))
                    else:
                        if q:
                            opening = q.popleft()
                            self.grid[opening[0]][opening[1]] = 'O'
                            self.grid[r][c] = '.'
                            q.append((r, c))
            # west
            for r in range(num_rows):
                q = deque()
                for c in range(num_cols):
                    next_point = self.grid[r][c]
                    if next_point == '#':
                        q = deque()
                    elif next_point == '.':
                        q.append((r, c))
                    else:
                        if q:
                            opening = q.popleft()
                            self.grid[opening[0]][opening[1]] = 'O'
                            self.grid[r][c] = '.'
                            q.append((r, c))
            # south
            for c in range(num_cols):
                q = deque()
                for r in range(num_rows - 1, -1, -1):
                    next_point = self.grid[r][c]
                    if next_point == '#':
                        q = deque()
                    elif next_point == '.':
                        q.append((r, c))
                    else:
                        if q:
                            opening = q.popleft()
                            self.grid[opening[0]][opening[1]] = 'O'
                            self.grid[r][c] = '.'
                            q.append((r, c))
            # east
            for r in range(num_rows):
                q = deque()
                for c in range(num_cols - 1, -1, -1):
                    next_point = self.grid[r][c]
                    if next_point == '#':
                        q = deque()
                    elif next_point == '.':
                        q.append((r, c))
                    else:
                        if q:
                            opening = q.popleft()
                            self.grid[opening[0]][opening[1]] = 'O'
                            self.grid[r][c] = '.'
                            q.append((r, c))

            for r in range(num_rows):
                for c in range(num_cols):
                    total += num_rows - r if self.grid[r][c] == 'O' else 0
            grid_state = ''.join(''.join(row) for row in self.grid)
            if grid_state in memo:
                # ok this print told me it repeats every 7 for the sample
                # for the input, it repeats every 14, so 1 billion mod 14 = 6
                # found the right one by solving 1,000,000,000 = 14x + *testing nums lol* from the following output
                print(memo[grid_state], 1_000_000_000 % memo[grid_state][1][0], (i + 1), (i + 1) % memo[grid_state][1][-1])
                if 1_000_000_000 % memo[grid_state][1][0] == 0 and (i + 1) % memo[grid_state][1][0] == 0:
                    return memo[grid_state][0]
                memo[grid_state][1].append((i + 1))
            else:
                memo[grid_state] = (total, [(i + 1)])


sol = Solution("input.txt")
print(sol.solve())
start = time.perf_counter()
print(sol.solve_b())
print((time.perf_counter() - start) * 1000000000)
