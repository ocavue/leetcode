"""
submits:
- date: 2021-01-16
  minutes: 5
  cheating: false
labels: [dp]
"""
#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (48.11%)
# Likes:    5613
# Dislikes: 178
# Total Accepted:    849.6K
# Total Submissions: 1.8M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#

# @lc code=start


def run():
    i = j = 1
    yield i
    yield j
    while True:
        k = i + j
        yield k
        i, j = j, k


class Solution:
    def climbStairs(self, n: int) -> int:
        for i in run():
            if n == 0:
                return i
            n -= 1


# @lc code=end

