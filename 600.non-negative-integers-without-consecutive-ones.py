"""
submits:
- date: 2020-08-23
  minutes: 48
  cheating: false
labels:
- dp
"""
#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (33.54%)
# Likes:    402
# Dislikes: 72
# Total Accepted:    12.5K
# Total Submissions: 36.5K
# Testcase Example:  '1'
#
# Given a positive integer n, find the number of non-negative integers less
# than or equal to n, whose binary representations do NOT contain consecutive
# ones.
#
# Example 1:
#
# Input: 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.


# @lc code=start

from typing import Tuple


dp_zeros = [0, 1]
dp_ones = [0, 1]


def find_int_by_bits(bits: int) -> Tuple[int, int]:
    """
    寻找在 bits 位内可以表示的所有数字。
    分别返回所有以 0 开头和以 1 开头的数字的数量。
    """
    assert bits >= 1

    if bits >= len(dp_zeros):

        for n in range(len(dp_zeros), bits + 1):
            dp_zeros.append(dp_zeros[n - 1] + dp_ones[n - 1])
            dp_ones.append(dp_zeros[n - 1])

            assert len(dp_zeros) == len(dp_ones) == n + 1

    return dp_zeros[bits], dp_ones[bits]


def find_int(num: int):
    if num == 0:
        return 1
    if num == 1:
        return 2
    if num == 2:
        return 3

    assert num >= 1

    count = 0
    bit: str = "{:b}".format(num)
    bits: int = len(bit)
    assert bit[0] == "1"

    # 寻找最高位是 0 的 bits 位数
    # （也就是寻找所有的 bits-1 位数组合）
    zeros, ones = find_int_by_bits(bits - 1)
    count += zeros + ones

    # 寻找最高位是 1，次高位是 0，且小于等于 num 的 bits 位数
    if bits > 2:
        if bit[1] == "1":
            count += sum(find_int_by_bits(bits - 2))
        else:
            count += find_int(int(bit[2:], 2))
    else:
        count += 1

    return count


class Solution:
    def findIntegers(self, num: int) -> int:
        return find_int(num)


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().findIntegers

    t.assertEqual(sum(find_int_by_bits(1)), 2)
    t.assertEqual(sum(find_int_by_bits(2)), 3)
    t.assertEqual(sum(find_int_by_bits(3)), 5)

    t.assertEqual(f(1), 2)
    t.assertEqual(f(2), 3)
    t.assertEqual(f(3), 3)
    t.assertEqual(f(4), 4)
    t.assertEqual(f(5), 5)
    t.assertEqual(f(6), 5)
