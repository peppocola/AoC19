from utils import fileSplitComma


def daytwo_part1():
    info = fileSplitComma('input//day2')
    integers = [int(e) for e in info]  # array with every integer from the file

    integers[1] = 12
    integers[2] = 2
    i = 0
    while 1:
        if integers[i] == 1:
            integers[integers[i + 3]] = integers[integers[i + 1]] + integers[integers[i + 2]]
            i = i + 4
        elif integers[i] == 2:
            integers[integers[i + 3]] = integers[integers[i + 1]] * integers[integers[i + 2]]
            i = i + 4
        elif integers[i] == 99:
            break
    return integers[0]


def daytwo_part2():
    info = fileSplitComma('input//day2')
    numbers = [int(e) for e in info]  # array with every integer from the file

    for noun in range(0, 100):
        for verb in range(0, 100):
            temp = numbers.copy()
            temp[1] = noun
            temp[2] = verb

            i = 0
            while 1:
                if temp[i] == 1:
                    temp[temp[i + 3]] = temp[temp[i + 1]] + temp[temp[i + 2]]
                elif temp[i] == 2:
                    temp[temp[i + 3]] = temp[temp[i + 1]] * temp[temp[i + 2]]
                elif temp[i] == 99:
                    temp[i] += 1
                    break
                temp[i] += 4
                i = i + 4

            if temp[0] == 19690720:
                return 100 * noun + verb
    return 0


if __name__ == "__main__":
    print("part1=" + str(daytwo_part1()))
    print("part2=" + str(daytwo_part2()))
