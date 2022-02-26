import string


def read_input():
    with open("input.txt", "r") as fp:
        data = []
        for line in fp.readlines():
            halves = line.split("|")
            data.append([halves[0].rstrip().split(), halves[1].rstrip().split()])
        return data


# 7 segment display
#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

# 0: 6
# 1: 2
# 2: 5
# 3: 5
# 4: 4
# 5: 5
# 6: 6 -
# 7: 3
# 8: 7
# 9: 6 -

# 3 seg - 2 seg = a
# 4 seg - 2 seg = b d
# 6 seg - 4 seg - a = if 1 remains g
# 7 seg - 6 seg = c if in 7 or e if not


def s_str(str1, str2):
    return ''.join(set(str1).difference(set(str2)))


def c_str(str1, str2):
    # check if str1 contains elements from str2
    if set(str1) <= set(str2):
        return True
    else:
        return False


def decoder(code):
    seg_groups = dict.fromkeys([i for i in range(2, 8)])
    segments = dict.fromkeys(string.ascii_letters[0:7])

    for grp in range(2, 8):
        seg_groups[grp] = []

    for x in code:
        seg_groups[len(x)].append(x)

    # Decoding segment a
    segments["a"] = s_str(seg_groups[3][0], seg_groups[2][0])

    # Decoding segment e
    for seg in seg_groups[6]:
        tmp = s_str(s_str(seg, seg_groups[4][0]), segments["a"])
        if len(tmp) == 1:
            segments['g'] = tmp

    # Decoding segment c and e
    # for seg in seg_groups[6]:
    #     if c_str():

    print(segments)
    print(seg_groups)


def main():
    data = read_input()
    print(data)

    # count = 0
    # for x in data:
    #     count += len([string for string in x[1] if (len(string) == 2 or
    #                                                 len(string) == 4 or
    #                                                 len(string) == 3 or
    #                                                 len(string) == 7)])
    for line in data:
        decoder(line[0])
        break


if __name__ == '__main__':
    main()
