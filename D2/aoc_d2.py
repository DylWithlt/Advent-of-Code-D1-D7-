import pandas as pd

df = pd.read_csv("input.txt", sep=" ", header=None)
df.columns = ["direction", "value"]

horiz = 0
depth = 0
aim = 0

for index, row in df.iterrows():

    if row["direction"] == "up":
        aim -= row["value"]
    elif row["direction"] == "down":
        aim += row["value"]
    elif row["direction"] == "forward":
        horiz += row["value"]
        depth += aim * row["value"]

    print(depth, horiz)

print(depth * horiz)
