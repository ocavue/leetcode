"""
submits:
- date: 2020-09-27
  minutes: 3
  cheating: false
"""
#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (32.36%)
# Likes:    400
# Dislikes: 335
# Total Accepted:    57.9K
# Total Submissions: 175.1K
# Testcase Example:  '8'
#
#
# Given a positive integer n and you can do operations as follow:
#
#
#
#
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
#
#
#
#
# What is the minimum number of replacements needed for n to become 1?
#
#
#
#
# Example 1:
#
# Input:
# 8
#
# Output:
# 3
#
# Explanation:
# 8 -> 4 -> 2 -> 1
#
#
#
# Example 2:
#
# Input:
# 7
#
# Output:
# 4
#
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
#
#
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1),)


# @lc code=end

