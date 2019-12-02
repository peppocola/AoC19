def fileSplitLines(fname):
    with open(fname, "r") as f:
        return f.read().strip().splitlines()


def fileSplitComma(fname):
    with open('input//day2', "r") as f:
        return f.read().split(',')
