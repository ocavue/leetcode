"""
submits:
  - date: 2020-04-22
    cheating: false
"""

#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (52.76%)
# Likes:    3773
# Dislikes: 467
# Total Accepted:    280.5K
# Total Submissions: 528.5K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
#
# Input: [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: [3,1,3,4,2]
# Output: 3
#
# Note:
#
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
#
#
#

from typing import List

# @lc code=start


def find_duplicate_v1(nums: List[int]) -> int:
    """
    Time: O(n * log(n))
    Space: O(1)
    """
    n = len(nums) - 1

    def find(x: int, y: int) -> int:
        # find target
        # 1 <= x <= target < y <= n + 1

        if x == y - 1:
            return x
        else:
            target = (x + y) // 2
            lt_count = 0
            gt_count = 0
            for num in nums:
                if num < target:
                    lt_count += 1
                else:
                    gt_count += 1
            if lt_count >= target:
                return find(x, target)
            elif gt_count > n - target:
                return find(target, y)
            else:
                return target

    return find(1, n + 1)


def find_duplicate_v2(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)

    Use leetcode No.142
    """
    step_i = 0
    step_j = 0
    idx_i = nums[0]
    idx_j = nums[0]
    while True:
        idx_i = nums[idx_i]
        idx_j = nums[nums[idx_j]]
        step_i += 1
        step_j += 2
        if idx_i == idx_j:
            step_i = step_j
            break

    idx_y = idx_i
    del idx_i, step_i, idx_j, step_j

    idx_x = nums[0]

    while True:
        if idx_x == idx_y:
            return idx_x
        idx_x = nums[idx_x]
        idx_y = nums[idx_y]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return find_duplicate_v1(nums)


# @lc code=end
if __name__ == "__main__":
    s = Solution().findDuplicate
    import unittest

    test = unittest.TestCase("__init__")

    for f in [find_duplicate_v1, find_duplicate_v2]:
        test.assertEqual(f([1, 3, 4, 2, 2]), 2)
        test.assertEqual(f([3, 1, 3, 4, 2]), 3)
        test.assertEqual(f([1, 1]), 1)
        test.assertEqual(f([1, 2, 2]), 2)
