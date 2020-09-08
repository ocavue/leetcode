"""
submits:
- date: 2020-09-08
  minutes: 27
  cheating: false
comment: |
  这道题我一开始没想到，最后输出的结果中应该使用 K 而不是 13。说明应该认真看题。
"""

import itertools


def calcute(n1, o1, n2, o2, n3, o3, n4):
    return eval("(({n1}{o1}{n2}){o2}{n3}){o3}{n4}".format(n1=n1, o1=o1, n2=n2, o2=o2, n3=n3, o3=o3, n4=n4).replace("/", "//"))


def is_equal_24(num):
    return abs(num - 24) < 0.000001


def main(string: str):
    items = string.split(" ")
    map = {
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 1,
        "2": 2,
    }
    rmap = {v: k for k, v in map.items()}
    nums = []
    try:
        for item in items:
            nums.append(map[item])
    except KeyError:
        return "ERROR"

    # n1, n2, n3, n4 = nums
    for n1, n2, n3, n4 in itertools.permutations(nums, 4):
        # print(">", n1, n2, n3, n4)
        for o1 in "+-*/":
            for o2 in "+-*/":
                for o3 in "+-*/":
                    result = calcute(n1, o1, n2, o2, n3, o3, n4)
                    if is_equal_24(result):
                        return "{n1}{o1}{n2}{o2}{n3}{o3}{n4}".format(
                            n1=rmap[n1], o1=o1, n2=rmap[n2], o2=o2, n3=rmap[n3], o3=o3, n4=rmap[n4]
                        )

    return "NONE"


for inp, out in [
    ["A 2 3 4", "1+2+3*4"],
    ["6 6 6 6", "6+6+6+6"],
    ["A A A A", "NONE"],
    ["10 2 4 4", "10/2*4+4"],
    ["1 1 1 JOKER", "ERROR"],
]:
    r = main(inp)
    assert r == out, "{} != {}".format(r, out)

