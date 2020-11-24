"""
submits:
- date: 2020-11-24
  minutes: 10
  cheating: false
"""
#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (44.12%)
# Likes:    519
# Dislikes: 123
# Total Accepted:    72.8K
# Total Submissions: 164.7K
# Testcase Example:  '26'
#
#
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two’s complement method is used.
#
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
#
#
#
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
#
#
#
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"
#
#
#

# @lc code=start

n10_to_n16 = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            return self.toHex((((2 ** 32) - 1) ^ (-num)) + 1)

        a, b = divmod(num, 16)
        if a == 0:
            return n10_to_n16[b]
        else:
            return self.toHex(a) + n10_to_n16[b]


# @lc code=end
from tool import t

f = Solution().toHex
t(f(0), "0")
t(f(1), "1")
t(f(9), "9")
t(f(10), "a")
t(f(26), "1a")
t(f(-1), "ffffffff")

