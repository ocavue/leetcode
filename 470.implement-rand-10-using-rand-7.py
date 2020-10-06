"""
submits:
- date: 2020-10-06
  minutes: 5
  cheating: true
"""

#
# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#
# https://leetcode.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (45.98%)
# Likes:    617
# Dislikes: 214
# Total Accepted:    43.1K
# Total Submissions: 94.2K
# Testcase Example:  '1'
#
# Given the API rand7() that generates a uniform random integer in the range
# [1, 7], write a function rand10() that generates a uniform random integer in
# the range [1, 10]. You can only call the API rand7(), and you shouldn't call
# any other API. Please do not use a language's built-in random API.
#
# Each test case will have one internal argument n, the number of times that
# your implemented function rand10() will be called while testing. Note that
# this is not an argument passed to rand10().
#
# Follow up:
#
#
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
#
#
#
# Example 1:
# Input: n = 1
# Output: [2]
# Example 2:
# Input: n = 2
# Output: [2,8]
# Example 3:
# Input: n = 3
# Output: [3,8,10]
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1

# @lc code=end

