# sum of ids of games where no round has > 12r, >13g or >14b
import re


def day2a():
    lines = open("input.txt", "r").read().split("\n")
    print(lines)

    total = 0

    for i, line in enumerate(lines):
        rounds = line.split(": ")[1].split(";")
        v = True
        for r in rounds:
            red = re.findall(r'\d+\sred', r)
            green = re.findall(r'\d+\sgreen', r)
            blue = re.findall(r'\d+\sblue', r)
            v = v and valid([int(red[0][0:-4]) if red else 0, int(green[0][0:-6]) if green else 0,
                             int(blue[0][0:-5]) if blue else 0])
        if v:
            total += (i + 1)

    print(total)


def valid(nums):
    return nums[0] <= 12 and nums[1] <= 13 and nums[2] <= 14


day2a()
