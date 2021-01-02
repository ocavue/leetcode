"""
submits:
- date: 2021-01-01
  minutes: 96
  cheating: false
"""
#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (30.13%)
# Likes:    8595
# Dislikes: 1325
# Total Accepted:    803.2K
# Total Submissions: 2.6M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Example 3:
#
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
#
# Example 4:
#
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
#
# Example 5:
#
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

from typing import List


# @lc code=start

import bisect
import random


def get_random_item(*nums_list: List[int]):
    nums = random.choice([nums for nums in nums_list if nums])
    return random.choice(nums)


def get_num(nums: List[int], index: int, default):
    if 0 <= index < len(nums):
        return nums[index]
    else:
        return default


def get_median(nums: List[int]):
    # assertlen(nums) in [1, 2]
    return sum(nums) / len(nums)


def find(nums1: List[int], nums2: List[int], lo1: int, hi1: int, lo2: int, hi2: int, expected_head: int, expected_tail: int) -> float:
    if expected_head == 0 and expected_tail == 0:
        nums: List[int] = nums1[lo1:hi1] + nums2[lo2:hi2]
        return get_median(nums)

    # len1, len2 = hi1 - lo1, hi2 - lo2
    # assertexpected_head >= 0 or expected_tail >= 0
    # assertlen1 + len2 - expected_head - expected_tail in [1, 2]
    # assertlen1 > 0 or len2 > 0

    m = get_random_item(nums1, nums2)

    mi1, mj1 = bisect.bisect_left(nums1, m, lo1, hi1), bisect.bisect_right(nums1, m, lo1, hi1)
    mi2, mj2 = bisect.bisect_left(nums2, m, lo2, hi2), bisect.bisect_right(nums2, m, lo2, hi2)
    # assertlo1 <= mi1 <= mj1 <= hi1
    # assertlo2 <= mi2 <= mj2 <= hi2

    # assertall([x < m for x in nums1[lo1:mi1]]) and all([x == m for x in nums1[mi1:mj1]]) and all([x > m for x in nums1[mj1:hi1]])
    # assertall([x < m for x in nums2[lo2:mi2]]) and all([x == m for x in nums2[mi2:mj2]]) and all([x > m for x in nums2[mj2:hi2]])

    actual_head = (mi1 - lo1) + (mi2 - lo2)
    actual_body = (mj1 - mi1) + (mj2 - mi2)
    actual_tail = (hi1 - mj1) + (hi2 - mj2)

    # assertactual_head + actual_body + actual_tail == len1 + len2

    # print(f"nums[lo:hi] {nums1[lo1:hi1]} {nums2[lo2:hi2]} m: {m} actual_head: {actual_head} actual_tail: {actual_tail}")

    if 0 < actual_head <= expected_head:
        lo1 = mi1
        lo2 = mi2
        expected_head -= actual_head
        actual_head = 0

    if 0 < actual_tail <= expected_tail:
        hi1 = mj1
        hi2 = mj2
        expected_tail -= actual_tail
        actual_tail = 0

    # len1, len2 = hi1 - lo1, hi2 - lo2
    # assertactual_head + actual_body + actual_tail == len1 + len2
    if actual_head == 0 and actual_tail == 0:
        return m
    if actual_head + actual_body == actual_tail:
        return get_median(
            [
                max(get_num(nums1, mj1 - 1, float("-inf")), get_num(nums2, mj2 - 1, float("-inf")),),
                min(get_num(nums1, mj1, float("+inf")), get_num(nums2, mj2, float("+inf")),),
            ]
        )

    return find(nums1=nums1, nums2=nums2, lo1=lo1, lo2=lo2, hi1=hi1, hi2=hi2, expected_head=expected_head, expected_tail=expected_tail,)


def findMedianSortedArrays_v1(nums1: List[int], nums2: List[int]) -> float:
    if (len(nums1) + len(nums2)) % 2 == 0:
        expected_head = expected_tail = (len(nums1) + len(nums2)) // 2 - 1
    else:
        expected_head = expected_tail = (len(nums1) + len(nums2)) // 2

    return find(nums1, nums2, lo1=0, hi1=len(nums1), lo2=0, hi2=len(nums2), expected_head=expected_head, expected_tail=expected_tail)


###################################################################################################


def findMedianSortedArrays_v2(nums1: List[int], nums2: List[int]) -> float:
    pass


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return findMedianSortedArrays_v2(nums1, nums2)


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().findMedianSortedArrays

    import ipdb

    # ipdb.set_trace()

    for i in range(10):  # There is some random operations

        t(f([1, 3], [2]), 2)
        t(f([1, 2], [3, 4]), 2.5)
        t(f([0, 0], [0, 0]), 0)
        t(f([], [1]), 1)
        t(f([2], []), 2)
        t(f([1, 3], [2, 7]), 2.5)
        t(f([1, 2], [1, 2]), 1.5)

