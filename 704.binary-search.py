"""
submits:
- date: 2020-12-11
  minutes: 4
  cheating: false
labels:
- bisect
"""
#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (53.65%)
# Likes:    1009
# Dislikes: 53
# Total Accepted:    209.7K
# Total Submissions: 389.5K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
#
#
# Example 2:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
#
#
# Note:
#
#
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].
#
#
#

# @lc code=start
from bisect import bisect_right


class Solution:
    def search(self, nums, target: int) -> int:
        index = bisect_right(nums, target)
        if index <= 0 or index > len(nums):
            return -1
        if nums[index - 1] != target:
            return -1
        return index - 1


# @lc code=end
if __name__ == "__main__":
    f = Solution().search
    assert (f([-1, 0, 3, 5, 9, 12], 9)) == 4

