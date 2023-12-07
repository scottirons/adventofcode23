from heapq import heappop, heapify
from collections import Counter
import time


class Solution:
    def __init__(self, use_heap):
        self.conv = {
            'A': 13,
            'K': 12,
            'Q': 11,
            'J': 10,
            'T': 9,
            '9': 8,
            '8': 7,
            '7': 6,
            '6': 5,
            '5': 4,
            '4': 3,
            '3': 2,
            '2': 1
        }
        self.scoring = {
            (1, 1, 1, 1, 1): 0,
            (1, 1, 1, 2): 1,
            (1, 2, 2): 2,
            (1, 1, 3): 3,
            (2, 3): 4,
            (1, 4): 5,
            (5,): 6
        }
        self.heap = []
        self.score = 0
        self.use_heap = use_heap

    def score_and_format(self, card):
        counts = tuple(sorted([value for key, value in Counter(card[0]).items()]))  # for hashability's sake lul
        return self.scoring[counts], [self.conv[i] for i in card[0]], card[1]

    def process_input(self):
        with open('input.txt', 'r') as f:
            lines = f.read().split('\n')

        for line in lines:
            conv_line = line.split()
            self.heap.append(self.score_and_format((conv_line[0], int(conv_line[1]))))
        if self.use_heap:
            heapify(self.heap)
        else:
            self.heap.sort()

    def score_round(self):
        factor = 1
        if self.use_heap:
            while self.heap:
                self.score += (factor * heappop(self.heap)[2])
                factor += 1
        else:
            for val in self.heap:
                self.score += factor * val[2]
                factor += 1
        return self.score


total_a = 0
total_b = 0
for i in range(100):
    start_a = time.perf_counter()
    sol_a = Solution(True)
    sol_a.process_input()
    sol_a.score_round()
    total_a += (time.perf_counter() - start_a)

    start_b = time.perf_counter()
    sol_b = Solution(False)
    sol_b.process_input()
    sol_b.score_round()
    total_b += (time.perf_counter() - start_b)

print(f'The heap solution took on average {total_a / 100} seconds, while the other took {total_b / 100} seconds')
print(f'On average, using the heap is {(total_a / 100) - (total_b / 100)} seconds slower than just sorting the list')
