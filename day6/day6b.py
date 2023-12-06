import re
import time


def day6b():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")

    t = int(''.join(re.findall(r'\d+', lines[0])))
    d = int(''.join(re.findall(r'\d+', lines[1])))

    return sum((t - i) * i > d for i in range(1, t))


start_time = time.perf_counter()
print(f'Part 2 answer: {day6b()}')
print(f'Part 2 took {time.perf_counter() - start_time} seconds')
