import pandas as pd
import numpy as np
import re

grid = np.zeros((1002, 1002))


def read_input():
    inp = []
    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            res = re.findall("[\d]+", line)
            inp.append([int(i) for i in res])
    return inp


def process_input(inp_line):
    x1, y1, x2, y2 = inp_line

    left_pt = x1 < x2 and (x1, y1) or (x2, y2)
    right_pt = x1 < x2 and (x2, y2) or (x1, y1)

    if (x1 == x2) or (y1 == y2):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                grid[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                grid[y1][x] += 1
    else:

        slope = (left_pt[1] - right_pt[1]) / (left_pt[0] - right_pt[0])
        if slope == 1 or slope == -1:
            b = y1 - (slope * x1)

            for x in range(left_pt[0], right_pt[0] + 1):
                grid[round(slope * x + b)][x] += 1


def main():
    inp = read_input()

    # for test in range(min(944, 220), max(944, 220)):
    #     print(test)

    for line in inp:
        process_input(line)

    print(len(np.where(grid >= 2)[0]))


main()
