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

# @lc code=start
from typing import List
import heapq


def klargest(nums: List[int], k: int) -> int:
    """
    >>> klargest([0,1,2], 3)
    0
    >>> klargest([0,1,2,3], 3)
    1
    >>> klargest([0,1,2,3,4], 3)
    2
    >>> klargest([3,2,3,1,2,4,5,5,6], 4)
    4
    >>> klargest([3,2,1,5,6,4], 2)
    5
    """
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    assert 1 <= k == len(heap) <= len(nums)
    top_k = heap
    return min(top_k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return klargest(nums, k)


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
