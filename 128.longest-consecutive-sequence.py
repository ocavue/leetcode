"""
submits:
- date: 2021-01-18
  minutes: 10
  cheating: false
"""
#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (45.60%)
# Likes:    4511
# Dislikes: 218
# Total Accepted:    363.9K
# Total Submissions: 789.7K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# Follow up: Could you implement the O(n) solution?
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#

from typing import List

# @lc code=start

from functools import lru_cache


class Solution:
    def longestConsecutive(self, nums) -> int:
        s = set(nums)
        @lru_cache(None)
        def longest_consecutive(num):
            if num + 1 in s:
                return longest_consecutive(num + 1) + 1
            else:
                return 1

        best = 0
        for num in s:
            best = max(best, longest_consecutive(num))
        return best


# @lc code=end

