from utils import fileSplitLines


def daythree_part1():
    instructions = fileSplitLines('input//day3')
    wire1 = instructions[0].split(',')
    wire2 = instructions[1].split(',')

    matrix = {}
    intersections = []
    start = (0, 0)
    for i in wire1:
        for counter in range(0, int(i[1:])):
            start = move(i[0], start)
            matrix[start] = 0

    start = (0, 0)
    for i in wire2:
        for counter in range(0, int(i[1:])):
            start = move(i[0], start)
            if start in matrix:
                intersections.append(start)

    start = (0, 0)
    mindistance = manhattan(start, intersections[0])
    for i in intersections:
        new = manhattan(start, i)
        if new <= mindistance:
            mindistance = new
    return mindistance


def daythree_part2():
    instructions = fileSplitLines('input//day3')
    wire1 = instructions[0].split(',')
    wire2 = instructions[1].split(',')

    matrix = {}
    intersections = []
    start = (0, 0)
    steps = 0
    for i in wire1:
        for counter in range(0, int(i[1:])):
            start = move(i[0], start)
            steps += 1
            matrix[start] = steps

    start = (0, 0)
    steps = 0
    for i in wire2:
        for counter in range(0, int(i[1:])):
            start = move(i[0], start)
            steps += 1
            if start in matrix:
                intersections.append(start)
                matrix[start] += steps

    minsteps = matrix[intersections[0]]
    for i in intersections:
        if matrix[i] <= minsteps:
            minsteps = matrix[i]
    return minsteps


def moveleft(start):
    return start[0], start[1] - 1


def moveright(start):
    return start[0], start[1] + 1


def moveup(start):
    return start[0] - 1, start[1]


def movedown(start):
    return start[0] + 1, start[1]


def move(i, start):
    if i == 'R':
        return moveright(start)
    if i == 'L':
        return moveleft(start)
    if i == 'D':
        return movedown(start)
    if i == 'U':
        return moveup(start)


def manhattan(start, i):
    return abs(start[0] - i[0]) + abs(start[1] - i[1])


if __name__ == "__main__":
    print("part1=" + str(daythree_part1()))
    print("part2=" + str(daythree_part2()))
