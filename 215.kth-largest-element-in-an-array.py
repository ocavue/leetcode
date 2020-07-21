"""
submits:
  - date: 2020-04-28
    cheating: false
"""

"""
tags: [redo, quick-sort, quick-select, heap]
"""
#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (52.58%)
# Likes:    3154
# Dislikes: 222
# Total Accepted:    554.3K
# Total Submissions: 1M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
#

from typing import List

# @lc code=start
import heapq
import random


def klargest_v1(nums: List[int], k: int) -> int:
    """
    use heap
    time: O(n*log(k))
    space: O(k)

    >>> klargest_v1([0,1,2], 3)
    0
    >>> klargest_v1([0,1,2,3], 3)
    1
    >>> klargest_v1([0,1,2,3,4], 3)
    2
    >>> klargest_v1([3,2,3,1,2,4,5,5,6], 4)
    4
    >>> klargest_v1([3,2,1,5,6,4], 2)
    5
    """
    heap: List[int] = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    assert 1 <= k == len(heap) <= len(nums)
    top_k = heap
    return min(top_k)


def partition(nums: List[int], lo: int, hi: int) -> int:
    """

    >>> l = [0,4,3,2,1]
    >>> partition(l, 0, 5)
    1
    >>> print(l)
    [0, 1, 3, 2, 4]
    >>> l = [0,1,2,3]
    >>> partition(l, 0, 4)
    3
    """
    # assert 0 <= lo < hi <= len(nums)
    # assert hi - lo >= 2

    p = lo
    s = nums[hi - 1]  # s for split
    for x in range(lo, hi):
        if nums[x] < s:
            nums[p], nums[x] = nums[x], nums[p]
            p += 1
    nums[p], nums[hi - 1] = nums[hi - 1], nums[p]

    # small_part = nums[lo:p]
    # large_part = nums[p + 1 : hi]
    # assert all([n < s for n in small_part]), f"{small_part}, {s}"
    # assert all([n >= s for n in large_part]), f"{large_part}, {s}"
    # assert nums[p] == s

    return p


random.seed(a=12345)


def klargest_v2(nums: List[int], k: int) -> int:
    """
    use quick-select
    quick-select 和 quick-sort 很相似，但是由于 quick-select 只需要处理分割后的一半的数据，会比 quick-sort 快很多

    spece: O(1) (write in-place)
    time:
        Worst-case performance: О(n^2)
        Best-case performance: О(n)
        Average performance: O(n)

    >>> klargest_v2([0,1,2], 3)
    0
    >>> klargest_v2([0,1,2,3], 3)
    1
    >>> klargest_v2([0,1,2,3,4], 3)
    2
    >>> klargest_v2([3,2,3,1,2,4,5,5,6], 4)
    4
    >>> klargest_v2([3,2,1,5,6,4], 2)
    5
    >>> klargest_v2([99,99,99,99,99], 1)
    99
    """

    random.shuffle(nums)

    def quick_select_klarget(lo: int, hi: int, k: int):
        # assert 0 <= lo < hi <= len(nums)

        if lo + 1 == hi:
            return nums[lo]

        p = partition(nums, lo, hi)

        large_part_length = hi - p - 1
        # small_part_length = p - lo
        # assert small_part_length + large_part_length + 1 == hi - lo

        # 注意在使用 quick-sort / quick-select 时，必须要分成三分，不然面对 [99,99,99,99] 这种所有元素都相同的情况会死循环
        if large_part_length == k - 1:
            return nums[p]
        elif large_part_length >= k:
            return quick_select_klarget(p + 1, hi, k)
        else:
            return quick_select_klarget(lo, p, k - large_part_length - 1)

    return quick_select_klarget(0, len(nums), k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return klargest_v2(nums, k)


# @lc code=end
if __name__ == "__main__":
    DEBUG = True
    import doctest

    doctest.testmod()
