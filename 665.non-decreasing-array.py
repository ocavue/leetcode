"""
submits:
- date: 2020-12-28
  minutes: 11
  cheating: false
"""
#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.54%)
# Likes:    2307
# Dislikes: 550
# Total Accepted:    113K
# Total Submissions: 576.9K
# Testcase Example:  '[4,2,3]'
#
# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).
#
#
# Example 1:
#
#
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
#
#
# Example 2:
#
#
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10 ^ 4ƒ
# - 10 ^ 5 <= nums[i] <= 10 ^ 5
#
#
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int], max_replacement=1) -> bool:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if max_replacement <= 0:
                    return False

                # case1: decrease nums[i]
                prev_i = nums[i]
                nums[i] = nums[i + 1]
                if self.checkPossibility(nums, max_replacement - 1):
                    return True
                nums[i] = prev_i

                # case2: increase nums[i+1]
                prev_i1 = nums[i + 1]
                nums[i + 1] = nums[i]
                if self.checkPossibility(nums, max_replacement - 1):
                    return True
                nums[i + 1] = prev_i1

                max_replacement -= 1
                if max_replacement <= 0:
                    return False
        return True


# @lc code=end

