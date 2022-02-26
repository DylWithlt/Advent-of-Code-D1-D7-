import pandas as pd
import numpy as np

df = pd.read_csv("input.txt", sep=" ", dtype="string", header=None)[0].to_numpy()

bit_tracker = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in df:
    for bit in range(len(bit_tracker)):
        bit_tracker[bit] += (str(x)[bit] == "0" and 1 or -1)
print(bit_tracker)

bit_str = ''.join((e > 0 and str(1) or str(0)) for e in bit_tracker)
print(bit_str)


def flip_bits(binary):
    binary = str(bin(binary))[2:]
    new_binary = binary.replace('1', '2').replace('0', '1').replace('2', '0')
    return int(new_binary, 2)


gamma = bin(int(bit_str, 2))
epsilon = bin(flip_bits(int(bit_str, 2)))

print(gamma, epsilon)
print(int(gamma, 2), int(epsilon, 2))
print(int(gamma, 2) * int(epsilon, 2))
