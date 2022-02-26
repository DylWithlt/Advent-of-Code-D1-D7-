import copy

import pandas as pd
import numpy as np
import math
import numpy.ma as ma

df = pd.read_csv("input.txt", header=None, skiprows=[0])[0].to_numpy()

numbers = []
for x in df:
    numbers.append(np.fromstring(x, dtype=int, sep=' '))

numbers = np.array(numbers)
numbers = np.vsplit(numbers, numbers.shape[0] / 5)

bingo_boards = []


class BingoBoard:
    def __init__(self, board, num):
        self.tracker = np.zeros((5, 5))
        self.board = board

    def __str__(self):
        return str(self.board)

    def process_call(self, _call):
        pos = np.where(self.board == _call)
        found_coords = np.array(pos).flatten()
        if len(found_coords) > 0:
            self.tracker[found_coords[0]][found_coords[1]] = 1

    def check_winner(self):
        for arr in self.tracker:
            if not (0 in arr):
                return True
        for arr in np.rot90(self.tracker):
            if not (0 in arr):
                return True
        return False


for x in range(len(numbers)):
    bingo_boards.append(BingoBoard(numbers[x], x))


def bingo_tester():
    bingo_boards[0].process_call(3)

    # bingo_boards[0].process_call(86)

    print(bingo_boards[0].tracker)
    print(bingo_boards[2].tracker)
    print(bingo_boards[0].check_winner())


with open("input.txt", "r") as fp:
    inputs = [int(x) for x in fp.readline().split(",")]

called_nums = []


def get_winner():
    for curr_call in inputs:
        called_nums.append(curr_call)
        for board in bingo_boards:
            board.process_call(curr_call)
            if board.check_winner():
                return [board, curr_call]


def get_last_winner():
    winners = []
    for curr_call in inputs:
        called_nums.append(curr_call)
        for board in bingo_boards:
            print(len(bingo_boards))
            board.process_call(curr_call)

        for board in bingo_boards:
            if board.check_winner():
                winners.append([board, curr_call])
                bingo_boards.remove(board)
    return winners.pop()


def main():
    winner_data = get_winner()
    print(called_nums)

    print('--------------------')

    mx = ma.masked_array(winner_data[0].board, mask=winner_data[0].tracker)

    print()
    print(winner_data[1])

    print(mx.sum() * winner_data[1])

    print('--------------------')
    print('----Part 2----------')

    last_win = get_last_winner()
    mx_last = ma.masked_array(last_win[0].board, mask=last_win[0].tracker)
    print(last_win[0])
    print(mx_last)
    print(mx_last.sum())
    print(last_win[1])
    print(mx_last.sum() * last_win[1])


main()
