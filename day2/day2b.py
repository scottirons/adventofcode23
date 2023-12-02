# sum of ids of games where no round has > 12r, >13g or >14b
import re


def day2b():
    lines = open("input.txt", "r").read().split("\n")

    total = 0

    for i, line in enumerate(lines):
        rounds = line.split(": ")[1].split(";")
        r, g, b = 0, 0, 0
        for rnd in rounds:
            red = re.findall(r'\d+\sred', rnd)
            green = re.findall(r'\d+\sgreen', rnd)
            blue = re.findall(r'\d+\sblue', rnd)
            r = max(int(red[0][0:-4]) if red else 0, r)
            g = max(int(green[0][0:-6]) if green else 0, g)
            b = max(int(blue[0][0:-5]) if blue else 0, b)
        total += (r * g * b)

    print(total)

day2b()
