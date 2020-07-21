"""
submits:
  - date: 2020-07-07
    cheating: false
"""

#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (44.51%)
# Likes:    1373
# Dislikes: 176
# Total Accepted:    123K
# Total Submissions: 272.6K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
#
# Example:
#
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
#
#
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
#
#

from typing import List

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1

        # index 是金额总和
        # value 是达到这个金额一共有多少总组合
        cache = [None for _ in range(target + 1)]

        # 达到总额为 0 的数字组合只有一种，就是一个空数字列表
        cache[0] = 1

        for sum in range(1, target + 1):
            combinations = 0
            for num in nums:
                if 0 <= sum - num <= target and cache[sum - num] is not None:
                    combinations += cache[sum - num]
            cache[sum] = combinations

        return cache[target]


# @lc code=end
t = Solution().combinationSum4

assert t([1, 2, 3], 4) == 7
