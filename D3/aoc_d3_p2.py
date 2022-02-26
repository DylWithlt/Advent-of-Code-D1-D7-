import pandas as pd
import numpy as np

df = pd.read_csv("input.txt", sep=" ", dtype="string", header=None)[0].to_numpy()


def get_popular_bit(data, bit, bias):
    popular_bit = 0

    for x in data:
        popular_bit += (1 if str(x)[bit] == "1" else -1)

    return 1 if popular_bit > 0 else 0 if popular_bit < 0 else 1


def get_most_common(data, bit, bias):
    most_common = []
    least_common = []

    popular_bit = str(get_popular_bit(data, bit, bias))

    for x in data:
        if str(x)[bit] == popular_bit:
            most_common.append(x)
        else:
            least_common.append(x)

    return most_common, least_common


def oxy_rating():
    bias = 1
    bit = 0

    most_pop, _ = get_most_common(df, bit, bias)
    while len(most_pop) > 1 and bit < 12:
        bit += 1
        most_pop, _ = get_most_common(most_pop, bit, bias)

    print(most_pop)
    return most_pop[0]


def co2_rating():
    bias = 0
    bit = 0

    _, least_pop = get_most_common(df, bit, bias)
    while len(least_pop) > 1 and bit < 12:
        bit += 1
        _, least_pop = get_most_common(least_pop, bit, bias)

    print(least_pop)
    return least_pop[0]


def main():
    oxy = oxy_rating()
    co2 = co2_rating()

    print(int(oxy, 2) * int(co2, 2))


main()