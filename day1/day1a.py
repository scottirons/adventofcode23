def day1a():
    input = open("input.txt", "r").read().split("\n")

    # part 1
    sum_a = 0
    for line in input:
        temp = []
        for char in line:
            if char.isdigit():
                temp.append(char)
        sum_a += int(temp[0] + temp[-1])

    print("part 1: " + str(sum_a))


day1a()
