#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (29.19%)
# Likes:    903
# Dislikes: 487
# Total Accepted:    76.4K
# Total Submissions: 260.6K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]....
#
# Example 1:
#
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
#
# Example 2:
#
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#

# @lc code=start

from typing import List
import random


def swap(nums: List[int], i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]


def quick_select(nums: List[int], lo: int, hi: int):
    """
    从 nums[lo:hi] 中筛选出小于等于 target 个数字的
    """

    assert 0 <= lo < hi < len(nums)

    o = random.randint(lo, hi - 1)
    nums[o], nums[lo] = nums[lo], nums[o]
    num = nums[o]

    # nums[lo + 1:i] 中的所有数字都是小于 num 的
    # nums[i:j]      中的所有数字都是等于 num 的
    # nums[k:hi]     中的所有数字都是大于 num 的
    i = j = lo + 1
    k = hi

    def valid():
        assert all([x < num for x in nums[lo + 1 : i]])
        assert all([x == num for x in nums[i:j]])
        assert all([x > num for x in nums[k:hi]])

    valid()
    while j < k:
        valid()

        if nums[j] == num:
            j += 1
        elif nums[j] < num:
            swap(nums, i, j)
            i += 1
            j += 1
        else:
            swap(nums, j, k - 1)
            k -= 1

    assert j == k
    valid()

    lt_count = i - (lo + 1)
    eq_count = j - i
    gt_count = hi - k

    assert lt_count >= 0
    assert eq_count >= 0
    assert gt_count >= 0

    i -= 1
    swap(nums, i, lo)
    eq_count += 1

    assert lt_count >= 0
    assert eq_count >= 1
    assert gt_count >= 0

    return lo, i, j, hi


def wiggle_sort(sorted: List[int]) -> None:
    half = len(sorted) // 2
    assert max(sorted[:half]) <= min(sorted[half:])


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

        # lo = 0
        # hi = len(nums)

        # while hi - lo >= 1:
        #     l, i, j, h = quick_select(nums, lo, hi)
        #     assert lo == l
        #     assert hi == h

        #     if i >= len(nums) // 2:
        #         lo = l
        #         hi = i
        #     elif j <= len(nums) // 2:
        #         lo = j
        #         hi = h
        #     else:
        #         break


# @lc code=end

if __name__ == "__main__":
    f = Solution().wiggleSort
    nums = [1, 5, 1, 1, 6, 4]
    f(nums)
    assert nums == [1, 6, 1, 5, 1, 4], nums

    nums = [1, 3, 2, 2, 3, 1]
    f(nums)
    assert nums == [2, 3, 1, 3, 1, 2]

