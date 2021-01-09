"""
submits:
- date: 2020-01-09
  minutes: 3
  cheating: false
labels:
- dp
"""
#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (42.49%)
# Likes:    6108
# Dislikes: 182
# Total Accepted:    636.8K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

from typing import List

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1] * len(nums)

        # rob nums[index:]
        def r(index: int) -> int:
            if index >= len(nums):
                return 0
            if dp[index] != -1:
                return dp[index]
            val = nums[index]
            res = max(val + r(index + 2), r(index + 1))
            dp[index] = res
            return res

        for i in range(len(nums) - 1, -1, -1):
            r(i)

        return r(0)


# @lc code=end

