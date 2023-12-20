import time
from collections import deque
from math import lcm


def parse_input(source):
    d = {}
    s = {}
    c = {}
    with open(source, 'r') as f:
        lines = f.read().split('\n')
    for line in lines:
        key, ins = line.split(' -> ')
        ins = ins.split(', ')
        if '%' in key:
            d[key[1:]] = ins
            c[key[1:]] = False
        elif '&' in key:
            d[key[1:]] = ins
            s[key[1:]] = {}
        else:
            d[key] = ins
            c[key] = False
    # map the sources for the & ones
    for key, values in d.items():
        for val in values:
            if val in s:
                s[val][key] = False
    return d, s, c


def main(source):
    dest, src, curr = parse_input(source)
    pulses = deque()
    high_pulses = 0
    low_pulses = 0
    presses = 0
    gf_lens = {}
    while True:
        if presses == 1000:
            print(f'Part 1: {high_pulses * low_pulses}')
        presses += 1
        pulses.append(('button', 'broadcaster', False))
        while pulses:
            s, d, high_pulse = pulses.popleft()
            if d == 'gf' and high_pulse and s not in gf_lens:
                gf_lens[s] = presses
                if len(gf_lens) == len(src['gf']):
                    print(f'Part 2: {lcm(*[val for _, val in gf_lens.items()])}')
                    return
            if high_pulse:
                high_pulses += 1
            else:
                low_pulses += 1
            if d == 'broadcaster':
                for val in dest['broadcaster']:
                    pulses.append(('broadcaster', val, False))
            # it's a toggle one
            elif d not in src:
                # it's a low pulse
                if not high_pulse and d in dest:
                    curr[d] = not curr[d]
                    for val in dest[d]:
                        pulses.append((d, val, curr[d]))
            # it has sources to keep track of
            else:
                src[d][s] = high_pulse
                send = not all(src[d][key] for key in src[d])
                for val in dest[d]:
                    pulses.append((d, val, send))


if __name__ == "__main__":
    start = time.perf_counter()
    main('input.txt')
    print(f'This whole shenanigan took {round(time.perf_counter() - start, 4)} seconds')
