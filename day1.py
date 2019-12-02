from utils import fileSplitLines


def dayone_part1():
    ch = fileSplitLines(
        'input\\day1')  # string with all the file values, there is a number per line
    mass = [(int(e)) for e in ch]  # array with every number from the file
    result = 0
    for i in mass:
        result += calcfuel(i)
    return result


def dayone_part2():
    ch = fileSplitLines(
        'input\\day1')  # string with all the file values, there is a number per line
    mass = [(int(e)) for e in ch]  # array with every number from the file

    totalFuel = 0

    for i in mass:
        fuel = calcfuel(i)
        while fuel > 0:
            totalFuel += fuel
            fuel = calcfuel(fuel)

    return totalFuel


def calcfuel(fuel):
    return fuel // 3 - 2


if __name__ == "__main__":
    print("part1="+str(dayone_part1()))
    print("part2="+str(dayone_part2()))
