# I NEED IT!

import re
from collections import defaultdict
INFILE = "input.txt"
SPLIT_INDEX = 11


def day4b():
    cards = []
    copies = defaultdict(int)
    with open(INFILE, "r") as infile:
        for i, line in enumerate(infile):
            cards.append(re.findall(r'\d+', line))
            copies[i + 1] = 1

    for card in cards:
        num_wins = 0
        my_card = card[SPLIT_INDEX:]
        for i in range(1, SPLIT_INDEX):
            if card[i] in my_card:
                num_wins += 1

        for i in range(num_wins):
            copies[int(card[0]) + i + 1] += (1 * copies[int(card[0])])

    print(sum(copies[i] for i in range(1, len(cards) + 1)))


day4b()
