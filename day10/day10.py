import math


class Solution:
    def __init__(self, source):
        self.grid = self.parse_input(source)
        self.start = self.find_start()
        self.route = [self.start]

    @staticmethod
    def parse_input(source):
        with open(source, "r") as f:
            return f.read().split('\n')

    def find_start(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'S':
                    return [i, j]

    @staticmethod
    def find_next_direction(start, letter):
        if letter == "F":
            if start == (-1, 0):
                return 0, 1
            return 1, 0
        elif letter in "|-":
            return start
        elif letter == "7":
            if start == (0, 1):
                return 1, 0
            return 0, -1
        elif letter == "J":
            if start == (1, 0):
                return 0, -1
            return -1, 0
        elif letter == "L":
            if start == (1, 0):
                return 0, 1
            return -1, 0

    def part_a(self):
        # looking at the chart, it starts here, it's a 7 above it
        curr_loc = [self.start[0] - 1, self.start[1]]
        curr_dir = (0, -1)

        while curr_loc != self.start:
            self.route.append(curr_loc)
            curr_loc = [curr_loc[0] + curr_dir[0], curr_loc[1] + curr_dir[1]]
            curr_letter = self.grid[curr_loc[0]][curr_loc[1]]
            curr_dir = self.find_next_direction(curr_dir, curr_letter)

        return math.ceil(len(self.route) / 2)


sol = Solution("input.txt")
print(sol.part_a())

