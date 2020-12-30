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
# Follow up: The overall run time complexity should be O( ).
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

# @lc code=start

from typing import List
import bisect

THRESHOLD = 10


def find(nums1: List[int], nums2: List[int], lo1: int, hi1: int, lo2: int, hi2: int, expected_left: int, expected_right: int) -> float:

    len1 = hi1 - lo1
    len2 = hi2 = lo2

    if len1 > len2:
        nums1, nums2 = nums2, nums1
        lo1, lo2 = lo2, lo1
        hi1, hi2 = hi2, hi1

        len1 = hi1 - lo1
        len2 = hi2 = lo2

    assert len1 <= len2

    mi2 = lo2 + ((hi2 - lo2) // 2)
    mi1 = bisect.bisect_right(nums1, mi2, lo1, hi1)

    assert 0 <= lo1 <= mi1 <= hi1 <= len(nums1)
    assert 0 <= lo2 <= mi2 <= hi2 <= len(nums2)

    assert nums1 and nums2
    m = nums2[-1] if mi2 == len(nums2) else nums2[mi2]

    assert all([i <= m for i in nums1[0:mi1]]), f"A nums1: {nums1}, mi1: {mi1}, m: {m}"
    assert all([i <= m for i in nums2[0:mi2]]), f"B nums2: {nums1}, mi2: {mi1}, m: {m}"
    assert all([i >= m for i in nums1[mi1 + 1 :]]), f"C nums1: {nums1}, mi1: {mi1}, m: {m}"
    assert all([i >= m for i in nums2[mi2 + 1 :]]), f"D nums2: {nums1}, mi2: {mi1}, m: {m}"

    actual_left = mi1 + mi2
    actual_right = len(nums1) + len(nums2) - actual_left

    if actual_left < expected_left - THRESHOLD:
        lo1 = mi1
        lo2 = mi2
        return find(nums1, nums2, lo1, hi1, lo2, hi2, expected_left, expected_right)
    elif actual_right < expected_right - THRESHOLD:
        hi1 = mi1
        hi2 = mi2
        return find(nums1, nums2, lo1, hi1, lo2, hi2, expected_left, expected_right)
    else:
        return try_find(nums1, nums2, mi1, mi2, expected_left, expected_right)


def try_find(nums1: List[int], nums2: List[int], m1: int, m2: int, expected_left: int, expected_right: int):
    lo1, hi1 = max(0, m1 - THRESHOLD), min(len(nums1), m1 + THRESHOLD)
    lo2, hi2 = max(0, m2 - THRESHOLD), min(len(nums2), m2 + THRESHOLD)

    reset = sorted(nums1[lo1:hi1] + nums2[lo2:hi2])
    actual_left = lo1 + lo2
    actual_right = len(nums1) + len(nums2) - len(reset) - actual_left

    assert actual_left <= expected_left
    assert actual_right <= expected_right

    while actual_left < expected_left:
        reset = reset[1:]
        actual_left += 1
    while actual_right < expected_right:
        reset.pop()
        actual_right += 1
    assert len(reset) in [1, 2]
    return get_median(reset)


def get_median(nums: List[int]) -> float:
    if not nums:
        return 0
    if len(nums) % 2 == 0:
        m = len(nums) // 2
        return (nums[m - 1] + nums[m]) / 2.0
    else:
        return nums[len(nums) // 2]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 or not nums2:
            return get_median(nums1 or nums2)

        half = (len(nums1) + len(nums2)) // 2
        if (len(nums1) + len(nums2)) % 2 == 0:
            expected_left = half - 1
            expected_right = half - 1
        else:
            expected_left = expected_right = half

        assert len(nums1) + len(nums2) - expected_left - expected_right in [1, 2]

        return find(nums1, nums2, 0, len(nums1), 0, len(nums2), expected_left, expected_right)


# @lc code=end

if __name__ == "__main__":
    from tool import t

    f = Solution().findMedianSortedArrays
    t(f([1, 3], [2]), 2.0)
    t(f([1, 2], [3, 4]), 2.5)
    t(f([0, 0], [0, 0]), 0.0)
    t(f([1], []), 1)
    t(f([1, 3, 5, 7], [2, 4, 6]), 4)
    t(f([1, 3, 5, 7], [2, 4, 6, 8]), 4.5)
    t(f([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]), 0.0)

