class Solution:
    def __init__(self, source):
        with open(source, "r") as f:
            self.grid = f.read().split('\n')
        self.dir_key = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0)
        }

    def valid_point(self, point):
        if 0 <= point[0] < len(self.grid) and 0 <= point[1] < len(self.grid[0]):
            return True
        return False

    @staticmethod
    def new_dirs(curr_dir, char):
        # 0, 1, 2, 3 = right, down, left, up
        if char == '-':
            if curr_dir in [0, 2]:
                return [curr_dir]
            return [0, 2]
        elif char == '|':
            if curr_dir in [1, 3]:
                return [curr_dir]
            return [1, 3]
        elif char == '\\':
            if curr_dir == 1:
                return [0]
            elif curr_dir == 0:
                return [1]
            elif curr_dir == 2:
                return [3]
            elif curr_dir == 3:
                return [2]
        elif char == '/':
            if curr_dir == 0:
                return [3]
            elif curr_dir == 3:
                return [0]
            elif curr_dir == 2:
                return [1]
            elif curr_dir == 1:
                return [2]
        return [curr_dir]

    def solve(self, starting_point=(0, (0, 0))):
        stack = [starting_point]
        visited = {starting_point}  # direction, (coords). dirs = 0, 1, 2, 3 == r, d, l, u
        its_lit_fam = {starting_point[1]}
        while stack:
            curr_dir, curr_point = stack.pop()
            curr_char = self.grid[curr_point[0]][curr_point[1]]
            next_dirs = self.new_dirs(curr_dir, curr_char)
            for d in next_dirs:
                add = self.dir_key[d]
                new_point = (curr_point[0] + add[0], curr_point[1] + add[1])
                if self.valid_point(new_point):
                    its_lit_fam.add(new_point)
                    if (d, new_point) not in visited:
                        visited.add((d, new_point))
                        stack.append((d, new_point))
        return len(its_lit_fam)


sol = Solution('input.txt')
print(f'Part A: {sol.solve()}')
part_b_max = 0
# try rows from both directions
for i in range(len(sol.grid)):
    part_b_max = max(part_b_max, sol.solve((0, (i, 0))), sol.solve((2, (i, len(sol.grid[0]) - 1))))
# try cols from both directions
for j in range(len(sol.grid[0])):
    part_b_max = max(part_b_max, sol.solve((1, (0, j))), sol.solve((3, (len(sol.grid) - 1, j))))
print(f'Part b: {part_b_max}')
