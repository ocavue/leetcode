#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (27.52%)
# Likes:    1585
# Dislikes: 189
# Total Accepted:    165.6K
# Total Submissions: 597.2K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
#
# Example 1:
#
#
# Input: [10,2]
# Output: "210"
#
# Example 2:
#
#
# Input: [3,30,34,5,9]
# Output: "9534330"
#
#
# Note: The result may be very large, so you need to return a string instead of
# an integer.
#
#

from typing import List
from functools import cmp_to_key

# @lc code=start


def sort_cmp(a: str, b: str) -> float:
    if a == b:
        return 0

    if a + b < b + a:
        return -1
    else:
        return +1


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num = "".join(
            reversed(sorted([str(num) for num in nums], key=cmp_to_key(sort_cmp)))
        )
        return num if num[0] != '0' else '0'


# @lc code=end
if __name__ == "__main__":
    import unittest

    f = Solution().largestNumber

    t = unittest.TestCase("__init__")

    def test(nums: List[int], expected: str):
        return t.assertEqual(f(nums), expected)

    test([3, 30, 34, 5, 9], "9534330")
    test([10, 2], "210")
    test([0, 0], "0")
