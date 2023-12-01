def day1b():
    input = open("input.txt", "r").read().split("\n")

    # part 2
    sum_b = 0
    num_words = {"one": "o1ne", "two": "t2wo", "three": "t3hree", "four": "f4our", "five": "f5ive", "six": "s6ix",
                 "seven": "s7even", "eight": "e8ight", "nine": "n9ine"}
    for line in input:
        for num in num_words:
            if num in line:
                line = line.replace(num, num_words[num])
        temp = []
        for char in line:
            if char.isdigit():
                temp.append(char)
        sum_b += int(temp[0] + temp[-1])

    print("Part b: " + str(sum_b))


day1b()
