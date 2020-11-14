"""
submits:
- date: 2020-11-14
  minutes: 3
  cheating: false
"""
#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (43.76%)
# Likes:    1099
# Dislikes: 205
# Total Accepted:    380.3K
# Total Submissions: 869.1K
# Testcase Example:  '1'
#
# Given an integer n, return true if it is a power of two. Otherwise, return
# false.
#
# An integer n is a power of two, if there exists an integer x such that n ==
# 2^x.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: true
# Explanation: 2^0 = 1
#
#
# Example 2:
#
#
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
#
#
# Example 3:
#
#
# Input: n = 3
# Output: false
#
#
# Example 4:
#
#
# Input: n = 4
# Output: true
#
#
# Example 5:
#
#
# Input: n = 5
# Output: false
#
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        found_one = False
        for i in range(32, -1, -1):
            if (n >> i) & 1 == 1:
                if found_one:
                    return False
                else:
                    found_one = True
        return True


# @lc code=end
