def filescan(fname):
    with open(fname, "r") as f:
        return f.read().strip().splitlines()