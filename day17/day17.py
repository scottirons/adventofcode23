import time
from heapq import heapify, heappop, heappush


class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            self.grid = f.read().split('\n')
        # "straight", "left", "right"
        self.next_moves = {
            "r": ((0, 1, "r"), (-1, 0, "u"), (1, 0, "d")),
            "d": ((1, 0, "d"), (0, 1, "r"), (0, -1, "l")),
            "l": ((0, -1, "l"), (1, 0, "d"), (-1, 0, "u")),
            "u": ((-1, 0, "u"), (0, -1, "l"), (0, 1, "r"))
        }
        self.visited = [
            [
                {
                    "r": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    "d": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    "l": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    "u": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                }
                for _ in range(len(self.grid[0]))
            ]
            for _ in range(len(self.grid))
        ]
        self.heap = []
        self.sol_a = 999999999
        self.finish = (len(self.grid) - 1, len(self.grid[0]) - 1)

    def is_valid_point(self, point):
        return 0 <= point[0] < len(self.grid) and 0 <= point[1] < len(self.grid[0])

    def solve(self, part_b=False):
        # same direction
        min_moves = 4 if part_b else 0
        max_moves = 10 if part_b else 3
        self.heap.append((int(self.grid[0][1]), "r", (0, 1), 1))
        self.heap.append((int(self.grid[1][0]), "d", (1, 0), 1))
        heapify(self.heap)
        while self.heap:
            curr_score, curr_dir, curr_point, curr_len = heappop(self.heap)
            # we can try all directions
            if curr_len >= min_moves:
                for d in self.next_moves[curr_dir]:
                    next_len = curr_len + 1 if d[2] == curr_dir else 1
                    next_point = (curr_point[0] + d[0], curr_point[1] + d[1])
                    next_dir = d[2]
                    if next_len <= max_moves and self.is_valid_point(next_point):
                        next_score = curr_score + int(self.grid[next_point[0]][next_point[1]])
                        if next_point == self.finish:
                            self.sol_a = min(self.sol_a, next_score)
                            # idk we'll always find the solution the first time we get to the end
                            return
                        else:
                            if self.visited[next_point[0]][next_point[1]][next_dir][next_len] > next_score \
                                    or not self.visited[next_point[0]][next_point[1]][next_dir][next_len]:
                                self.visited[next_point[0]][next_point[1]][next_dir][next_len] = next_score
                                heappush(self.heap, (next_score, next_dir, next_point, next_len))
            # otherwise just try straight (dang this is very ugly oh well)
            else:
                d = self.next_moves[curr_dir][0]
                next_len = curr_len + 1 if d[2] == curr_dir else 1
                next_point = (curr_point[0] + d[0], curr_point[1] + d[1])
                next_dir = d[2]
                if next_len <= max_moves and self.is_valid_point(next_point):
                    next_score = curr_score + int(self.grid[next_point[0]][next_point[1]])
                    if next_point == self.finish:
                        self.sol_a = min(self.sol_a, next_score)
                        # idk we'll always find the solution the first time we get to the end
                        return
                    else:
                        if self.visited[next_point[0]][next_point[1]][next_dir][next_len] > next_score \
                                or not self.visited[next_point[0]][next_point[1]][next_dir][next_len]:
                            self.visited[next_point[0]][next_point[1]][next_dir][next_len] = next_score
                            heappush(self.heap, (next_score, next_dir, next_point, next_len))


start = time.perf_counter()
sol1 = Solution("input.txt")
sol2 = Solution("input.txt")
sol1.solve()
sol2.solve(True)
print(f'Part 1 answer: {sol1.sol_a}')
print(f'Part 2 answer: {sol2.sol_a}')
print(time.perf_counter() - start)
