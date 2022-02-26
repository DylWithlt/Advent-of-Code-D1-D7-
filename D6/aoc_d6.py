import pandas as pd
import numpy as np


def read_input():
    with open("input.txt", "r") as fp:
        return [int(i) for i in fp.readline().split(",")]


lantern_fish_tracker = dict.fromkeys([str(i) for i in range(9)])


def next_day():
    new_fish = lantern_fish_tracker[str(0)]

    for x in range(8):
        lantern_fish_tracker[str(x)] = lantern_fish_tracker[str(x + 1)]

    lantern_fish_tracker[str(8)] = 0

    lantern_fish_tracker[str(6)] += new_fish
    lantern_fish_tracker[str(8)] += new_fish


def main():
    lantern_fish = np.array(read_input())

    for x in range(9):
        lantern_fish_tracker[str(x)] = 0

    for fish in lantern_fish:
        lantern_fish_tracker[str(fish)] += 1

    print(lantern_fish_tracker)

    for x in range(256):
        next_day()

    print(sum(lantern_fish_tracker.values()))


main()
