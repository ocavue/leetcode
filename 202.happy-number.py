"""
submits:
  - date: 2020-04-30
    cheating: false
"""

#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (48.64%)
# Likes:    1829
# Dislikes: 390
# Total Accepted:    451.5K
# Total Submissions: 902.2K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.
#
# Example:
#
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
#

# @lc code=start


def is_happy(n: int, passed=None):

    if passed is None:
        passed = set()

    if n == 1:
        return True

    next = 0
    for i in str(n):
        next += int(i) ** 2

    if next in passed:
        return False
    else:
        passed.add(next)

    return is_happy(next, passed)


class Solution:
    def isHappy(self, n: int) -> bool:
        return is_happy(n)


# @lc code=end

if __name__ == "__main__":
    assert is_happy(19) is True
