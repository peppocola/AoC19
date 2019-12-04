def nondecreasing(a):
    return a == sorted(a)


def repeating(a):
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return 1
    return 0


def repeating2(a):
    i = 0
    repetition = 0
    while i < (len(a) - 1):

        if repetition == 1:
            if a[i] == a[i + 1]:
                repetition = 0
                i += 1
                while i < len(a) and a[i] == a[i - 1]:
                    i += 1
            else:
                return 1

        if (i < (len(a) - 1)) and (a[i] == a[i + 1]):
            repetition = 1

        i += 1

    return repetition


def dayfour_part1():
    with open('input//day4') as f:
        ch = f.read().strip().split('-')

    x, y = [int(num) for num in ch]

    result = 0

    return sum(nondecreasing(list(str(i))) and repeating(list(str(i))) for i in range(x, y))


def dayfour_part2():
    with open('input//day4') as f:
        ch = f.read().strip().split('-')

    x, y = [int(num) for num in ch]

    result = 0
    return sum(nondecreasing(list(str(i))) and repeating2(list(str(i))) for i in range(x, y))


if __name__ == "__main__":
    print("part1=" + str(dayfour_part1()))
    print("part2=" + str(dayfour_part2()))
