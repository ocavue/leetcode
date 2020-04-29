#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (50.35%)
# Likes:    1129
# Dislikes: 364
# Total Accepted:    308.7K
# Total Submissions: 610.1K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
#
#
# Note:
#
#
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
#
#
# Follow up:
#
#
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
#
#
#

# @lc code=start

from collections import defaultdict
from typing import List, Dict


def intersect_v1(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Your runtime beats 34.54 % of python3 submissions
    Your memory usage beats 5.72 % of python3 submissions (13.9 MB)
    """
    counts1: Dict[int, int] = defaultdict(int)
    counts2: Dict[int, int] = defaultdict(int)
    for n in nums1:
        counts1[n] += 1
    for n in nums2:
        counts2[n] += 1
    result = []
    for n, c1 in counts1.items():
        c2 = counts2[n]
        for i in range(min([c1, c2])):
            result.append(n)
    return result


def intersect_v2(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Your runtime beats 34.54 % of python3 submissions
    Your memory usage beats 5.72 % of python3 submissions (13.9 MB)
    """
    if not nums1 or not nums2:
        return []

    nums1.sort()
    nums2.sort()

    i, j = 0, 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return intersect_v2(nums1, nums2)


# @lc code=end
