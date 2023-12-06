import re
import time


def day6b():
    return sum((44826981 - i) * i > 202107611381458 for i in range(1, 44826981))


start_time = time.perf_counter()
print(f'Part 2 answer: {day6b()}')
print(f'Part 2 took {time.perf_counter() - start_time} seconds')
