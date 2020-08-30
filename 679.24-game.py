"""
submits:
- date: 2020-08-30
  minutes: 120
  cheating: false
"""
# 13:21
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#
# https://leetcode.com/problems/24-game/description/
#
# algorithms
# Hard (45.13%)
# Likes:    750
# Dislikes: 151
# Total Accepted:    41.9K
# Total Submissions: 90.1K
# Testcase Example:  '[4,1,8,7]'
#
#
# You have 4 cards each containing a number from 1 to 9.  You need to judge
# whether they could operated through *, /, +, -, (, ) to get the value of
# 24.
#
#
# Example 1:
#
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#
#
#
# Example 2:
#
# Input: [1, 2, 1, 2]
# Output: False
#
#
#
# Note:
#
# The division operator / represents real division, not integer division.  For
# example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use -
# as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression
# -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2,
# 1, 2], we cannot write this as 12 + 12.
#
#
#
#

# @lc code=start

from typing import List, Generator


def is_eqal(a, b) -> bool:
    return abs(a - b) < 0.000001


def calcute_2_nums(a: float, b: float) -> Generator[float, None, None]:
    yield a + b
    yield a - b
    yield b - a
    yield a * b
    if b != 0:
        yield (a / b)
    if a != 0:
        yield (b / a)


def calcute_3_nums(a: float, b: float, c: float) -> Generator[float, None, None]:
    for x in calcute_2_nums(b, c):
        yield from calcute_2_nums(a, x)
    for x in calcute_2_nums(a, c):
        yield from calcute_2_nums(b, x)
    for x in calcute_2_nums(a, b):
        yield from calcute_2_nums(c, x)


def calcute_4_nums(a: float, b: float, c: float, d: float) -> Generator[float, None, None]:
    for x in calcute_3_nums(b, c, d):
        yield from calcute_2_nums(a, x)
    for x in calcute_3_nums(a, c, d):
        yield from calcute_2_nums(b, x)
    for x in calcute_3_nums(a, b, d):
        yield from calcute_2_nums(c, x)
    for x in calcute_3_nums(a, b, c):
        yield from calcute_2_nums(d, x)

    for x in calcute_2_nums(a, b):
        for y in calcute_2_nums(c, d):
            yield from calcute_2_nums(x, y)
    for x in calcute_2_nums(a, c):
        for y in calcute_2_nums(b, d):
            yield from calcute_2_nums(x, y)
    for x in calcute_2_nums(a, d):
        for y in calcute_2_nums(b, c):
            yield from calcute_2_nums(x, y)


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        for result in calcute_4_nums(*nums):
            if is_eqal(result, 24):
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().judgePoint24
    t.assertTrue(f([4, 1, 8, 7]))
    t.assertFalse(f([1, 2, 1, 2]))
    t.assertFalse(f([1, 5, 9, 1]))
    t.assertTrue(f([1, 3, 4, 6]))
    t.assertTrue(f([1, 9, 1, 2]))

