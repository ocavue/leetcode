"""
submits:
- date: 2020-09-08
  minutes: 5
  cheating: false
"""

"""
提取不重复的整数

题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入
    9876673
输出
    37689
"""

from collections import defaultdict
from typing import List, Dict


def unique_sub_int(n: int):
    s = str(n)
    o: List[str] = []
    counter: Dict[str, int] = defaultdict(int)
    for i in range(len(s) - 1, -1, -1):
        char = s[i]
        counter[char] += 1
        if counter[char] == 1:
            o.append(char)
    return int("".join(o))

def run():
    print(unique_sub_int(int(input())))

if __name__ == "__main__":
    assert unique_sub_int(9876673) == 37689
