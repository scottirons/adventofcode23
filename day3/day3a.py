# bruh this is day 3? LOL
# just iterate the whole grid. If I find a digit, check all directions and add it to current num (*10 + int(num))

DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))


def day3a():
    # each line is a string of one line of words
    lines = open("input.txt", "r").read().split("\n")

    # helper function
    def valid_num(coord):
        valid = False
        for d in DIRS:
            row = coord[0] + d[0]
            col = coord[1] + d[1]
            # invalid coord doesn't matter
            if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
                continue
            # adjacent point is a symbol of any sort = the number is valid woohoo
            if not (lines[row][col]).isdigit() and lines[row][col] != '.':
                valid = True

        return valid

    total = 0

    for r in range(len(lines)):
        # set/reset current num for each row and reset valid bool
        curr_num = 0
        should_add = False
        for c, char in enumerate(lines[r]):

            # come across a non-digit and the current num we've been accumulating is valid
            if not char.isdigit():
                if should_add:
                    total += curr_num
                curr_num = 0
                should_add = False
            # it is a digit
            else:
                should_add = should_add or valid_num((r, c))
                curr_num = curr_num * 10 + int(char)
                # just in case our final digit here is the end of the row
                if c == len(lines[r]) - 1 and should_add:
                    total += curr_num

    print(total)


day3a()
