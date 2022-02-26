import pandas as pd
import numpy as np


def read_input():
    with open("input.txt", "r") as fp:
        return [int(i) for i in fp.readline().split(",")]


def find_least_fuel_align(data):
    fuel_costs = []
    for x in data:
        fuel_cost = 0
        for j in data:
            fuel_cost += sum(range(abs(x - j) + 1))
        fuel_costs.append(fuel_cost)
    return min(fuel_costs)


def main():
    inp = read_input()

    min_fuel = find_least_fuel_align(inp)

    print(min_fuel)


if __name__ == '__main__':
    main()
