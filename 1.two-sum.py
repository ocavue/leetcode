#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.12%)
# Likes:    13798
# Dislikes: 507
# Total Accepted:    2.6M
# Total Submissions: 5.8M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        for small_idx in range(0, len(nums)):
            small_num = nums[small_idx]
            for large_idx in range(small_idx + 1, len(nums)):
                large_num = nums[large_idx]
                if small_num + large_num == target:
                    return [small_idx, large_idx]


# @lc code=end
