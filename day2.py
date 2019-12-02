def daytwo_part1():
    with open('input//day2', "r") as f:
        numbers = f.read().split(',')
    integers = [int(e) for e in numbers]  # array with every integer from the file

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
    with open('input//day2', "r") as f:
        numbers = f.read().split(',')
    info = [int(e) for e in numbers]  # array with every integer from the file

    for noun in range(0, 100):
        for verb in range(0, 100):
            integers = info.copy()
            integers[1] = noun
            integers[2] = verb

            i = 0
            while 1:
                if integers[i] == 1:
                    integers[integers[i + 3]] = integers[integers[i + 1]] + integers[integers[i + 2]]
                elif integers[i] == 2:
                    integers[integers[i + 3]] = integers[integers[i + 1]] * integers[integers[i + 2]]
                elif integers[i] == 99:
                    integers[i] += 1
                    break
                integers[i] += 4
                i = i + 4

            if integers[0] == 19690720:
                return 100 * noun + verb
    return 0


if __name__ == "__main__":
    print("part1=" + str(daytwo_part1()))
    print("part2=" + str(daytwo_part2()))
