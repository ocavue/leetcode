"""
submits:
- date: 2020-11-16
  minutes: 5
  cheating: false
"""
#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (41.40%)
# Likes:    748
# Dislikes: 244
# Total Accepted:    211.8K
# Total Submissions: 511K
# Testcase Example:  '16'
#
# Given an integer n, return true if it is a power of four. Otherwise, return
# false.
#
# An integer n is a power of four, if there exists an integer x such that n ==
# 4^x.
#
#
# Example 1:
# Input: n = 16
# Output: true
# Example 2:
# Input: n = 5
# Output: false
# Example 3:
# Input: n = 1
# Output: true
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start


def can_divisible_by_four(n: int):
    return n % 4 == 0


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while True:
            if n == 1:
                return True

            a, b = divmod(n, 4)
            if b != 0:
                return False
            n = a
        return False


# @lc code=end
