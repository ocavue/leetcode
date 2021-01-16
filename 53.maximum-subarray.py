"""
submits:
- date: 2021-01-16
  minutes: 13
  cheating: false
labels: [dp]
"""
#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.00%)
# Likes:    10190
# Dislikes: 492
# Total Accepted:    1.3M
# Total Submissions: 2.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
#
#
# Example 3:
#
#
# Input: nums = [0]
# Output: 0
#
#
# Example 4:
#
#
# Input: nums = [-1]
# Output: -1
#
#
# Example 5:
#
#
# Input: nums = [-2147483647]
# Output: -2147483647
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
from typing import List

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        best = dp[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(nums[i], nums[i] + dp[i + 1])
            best = max(best, dp[i])

        return best


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().maxSubArray)
    t([[-2, 1, -3, 4, -1, 2, 1, -5, 4]], 6)

