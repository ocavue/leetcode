#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (56.35%)
# Likes:    3346
# Dislikes: 110
# Total Accepted:    737.3K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
#

from typing import List

# @lc code=start


def move0s(nums: List[int]) -> None:
    def switch(p, q):
        nums[p], nums[q] = nums[q], nums[p]

    first_zero = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            first_zero = i if first_zero == -1 else first_zero
        else:
            if first_zero == -1:
                pass
            else:
                switch(first_zero, i)
                first_zero += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return move0s(nums)


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    l = [0, 1, 0, 3, 12]
    move0s(l)
    t.assertEqual(l, [1, 3, 12, 0, 0])

    l = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    move0s(l)
    t.assertEqual(l, [1, 1, 1, 1, 1,0, 0, 0, 0, 0])

    l = [1, 4, 5, 3]
    move0s(l)
    t.assertEqual(l, [1, 4, 5, 3])

    l = [0, 0, 0]
    move0s(l)
    t.assertEqual(l, [0, 0, 0])

    l = []
    move0s(l)
    t.assertEqual(l, [])
