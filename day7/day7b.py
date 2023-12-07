from heapq import heappop, heapify
from collections import Counter


class Solution:
    def __init__(self):
        self.conv = {
            'A': 13,
            'K': 12,
            'Q': 11,
            'J': 0,
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

    def score_and_format(self, card):
        counts = Counter(card[0])
        seq = sorted([val for key, val in counts.items()])
        if 'J' in counts and len(seq) > 1:
            seq.remove(counts['J'])
            seq[-1] += counts['J']

        return self.scoring[tuple(seq)], [self.conv[i] for i in card[0]], card[1]

    def process_input(self):
        with open('input.txt', 'r') as f:
            lines = f.read().split('\n')

        for line in lines:
            conv_line = line.split()
            self.heap.append(self.score_and_format((conv_line[0], int(conv_line[1]))))
        heapify(self.heap)

    def score_round(self):
        factor = 1
        while self.heap:
            self.score += (factor * heappop(self.heap)[2])
            factor += 1
        return self.score


sol = Solution()
sol.process_input()
print(sol.score_round())

