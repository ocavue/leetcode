#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (59.03%)
# Likes:    2529
# Dislikes: 178
# Total Accepted:    335K
# Total Submissions: 564K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Note:
#
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
#
#
#

import heapq
from typing import List

# @lc code=start


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    >>> top_k_frequent([1,1,1,2,2,3], 2)
    [1, 2]
    >>> top_k_frequent([1], 1)
    [1]
    """
    counter = {}
    for num in nums:
        counter[num] = counter.setdefault(num, 0) + 1

    if k > len(nums):
        heap = [(count, num) for num, count in counter.items()]
        heapq.heapify(heap)
    else:
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
            assert len(heap) <= k

    assert len(heap) <= k
    return list(reversed([pair[1] for pair in heap]))


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return top_k_frequent(nums, k)


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
