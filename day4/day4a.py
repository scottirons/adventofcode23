import re


def day4a():
    cards = []
    with open("input.txt", "r") as infile:
        for line in infile:
            cards.append(re.findall(r'\d+', line))

    total = 0

    for card in cards:
        curr_score = 0
        my_card = card[11:]
        for i in range(1, 11):
            if card[i] in my_card:
                curr_score = curr_score * 2 if curr_score else 1
        total += curr_score

    print(total)


day4a()

