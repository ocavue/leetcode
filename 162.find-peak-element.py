#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (42.62%)
# Likes:    1388
# Dislikes: 1831
# Total Accepted:    322.2K
# Total Submissions: 754.1K
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and
# return its index.
#
# The array may contain multiple peaks, in that case return the index to any
# one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
#
# Example 2:
#
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2,
# or index number 5 where the peak element is 6.
#
#
# Note:
#
# Your solution should be in logarithmic complexity.
#
#

# @lc code=start
from typing import List
import math


def find_peak_element(nums: List[int]) -> int:

    def get_num(index: int):
        if index == -1:
            return -math.inf
        if index == len(nums):
            return -math.inf
        return nums[index]

    def search(start: int, end: int) -> int:
        assert start <= end
        if start == end:
            return start
        else:
            mid = (start + end) // 2
            if get_num(mid - 1) > get_num(mid):
                return search(start, mid - 1)
            elif get_num(mid) < get_num(mid + 1):
                return search(mid + 1, end)
            else:
                return mid

    return search(0, len(nums) - 1)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return find_peak_element(nums)


# @lc code=end

if __name__ == "__main__":
    assert find_peak_element([1, 2, 3, 1]) == 2
    assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) in [2, 5]
