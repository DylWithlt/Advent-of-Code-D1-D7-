import pandas as pd
import numpy as np

inp = pd.read_csv('input.txt', sep=" ", header=None)[0].to_numpy()

last_three = np.array([])

last_sum = inp[0] + inp[1] + inp[2]
increased = 0

for x in inp:

    last_three = np.append(last_three, x)
    if len(last_three) > 3:
        last_three = np.delete(last_three, 0)
    elif len(last_three) < 3:
        continue

    curr_sum = last_three.sum()

    print(curr_sum, (curr_sum > last_sum) and "(increased)" or
          (curr_sum < last_sum) and "(decreased)" or "(no change)")

    if curr_sum > last_sum:
        increased += 1

    last_sum = curr_sum

print(increased)

