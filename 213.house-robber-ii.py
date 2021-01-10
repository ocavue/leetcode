"""
submits:
- date: 2021-01-10
  minutes: 13
  cheating: false
labels:
- dp
"""
#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (36.64%)
# Likes:    2492
# Dislikes: 60
# Total Accepted:    222.3K
# Total Submissions: 594.5K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given a list of non-negative integers nums representing the amount of money
# of each house, return the maximum amount of money you can rob tonight without
# alerting the police.
#
#
# Example 1:
#
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2), because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 3:
#
#
# Input: nums = [0]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
#
#
#

from typing import List
from functools import lru_cache

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp1 = [-1] * len(nums)
        dp2 = [-1] * len(nums)

        def r(index: int, robbed_first: bool) -> int:
            if index >= len(nums):
                return 0
            elif robbed_first and dp1[index] != -1:
                return dp1[index]
            elif not robbed_first and dp2[index] != -1:
                return dp2[index]
            elif index == 0:
                dp1[index] = nums[index] + r(2, robbed_first=True)
                dp2[index] = r(1, robbed_first=False)
                return max(dp1[index], dp2[index])
            elif index == len(nums) - 1:
                if robbed_first:
                    dp1[index] = 0
                    return dp1[index]
                else:
                    dp2[index] = nums[index]
                    return dp2[index]
            else:
                res = max(nums[index] + r(index + 2, robbed_first), r(index + 1, robbed_first))
                if robbed_first:
                    dp1[index] = res
                else:
                    dp2[index] = res
                return res

        for i in range(len(nums)):
            r(i, True)
            r(i, False)

        return max(dp1[0], dp2[0])


# @lc code=end

