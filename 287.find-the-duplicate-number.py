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


def find_duplicate(nums: List[int]) -> int:
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


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return find_duplicate(nums)


# @lc code=end
if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]))
    print(find_duplicate([3, 1, 3, 4, 2]))
    print(find_duplicate([1, 1]))
    print(find_duplicate([1, 2, 2]))
