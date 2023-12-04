# bruh this is day 3? LOL
# just iterate the whole grid. If I find a digit, check all directions and add it to current num (*10 + int(num))
# ok but if the symbol happens to be an asterisk I gotta add the final number (once I finalize it) to a super secret
# hashmap?? While I'm searching maybe I can keep a list of any asterisks I find (just coordinates)
# modify valid_num to only return True if the symbol is an asterisk and ALSO return the coordinates of said asterisk lol

from collections import defaultdict

DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))


def day3a():
    # each line is a string of one line of words
    lines = open("input.txt", "r").read().split("\n")
    gear_dict = defaultdict(list[int])

    # helper function
    def valid_num(coord):
        valid = False
        asteriskzzz = []
        for d in DIRS:
            row = coord[0] + d[0]
            col = coord[1] + d[1]
            # invalid coord doesn't matter
            if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
                continue
            # adjacent point is a starry star
            if lines[row][col] == '*':
                valid = True
                asteriskzzz.append((row, col))

        return valid, asteriskzzz

    for r in range(len(lines)):
        # set/reset current num for each row and reset valid bool
        curr_num = 0
        touches_gearhead_from_rick_and_morty = False
        curr_gears = set()
        for c, char in enumerate(lines[r]):

            # come across a non-digit and the current num we've been accumulating touched any asterisks, add it to
            # the relevant keys in the dict
            if not char.isdigit():
                if touches_gearhead_from_rick_and_morty:
                    for gear in curr_gears:
                        gear_dict[gear].append(curr_num)
                curr_num = 0
                touches_gearhead_from_rick_and_morty = False
                curr_gears = set()
            # it is a digit
            else:
                v_from_cyberpunk, gears = valid_num((r, c))
                curr_gears = curr_gears.union(gears)
                touches_gearhead_from_rick_and_morty = touches_gearhead_from_rick_and_morty or v_from_cyberpunk
                curr_num = curr_num * 10 + int(char)
                # just in case our final digit here is the end of the row
                if c == len(lines[r]) - 1 and touches_gearhead_from_rick_and_morty:
                    for gear in curr_gears:
                        gear_dict[gear].append(curr_num)

    total = 0
    for gear, nums in gear_dict.items():
        if len(nums) == 2:
            total += nums[0] * nums[1]

    print(total)


day3a()
