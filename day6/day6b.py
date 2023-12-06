import re
import time


def day6b():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")

    times = re.findall(r'\d+', lines[0])
    distances = re.findall(r'\d+', lines[1])
    result = 1

    for i in range(len(times)):
        num_wins = 0
        for j in range(1, int(times[i]) + 1):
            if (int(times[i]) - j) * j > int(distances[i]):
                num_wins += 1
        result *= num_wins

    return result


start_time = time.perf_counter()
print(f'Part 2 answer: {day6b()}')
print(f'Part 2 took {time.perf_counter() - start_time} seconds')