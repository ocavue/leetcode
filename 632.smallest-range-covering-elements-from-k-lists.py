"""
submits:
- date: 2020-09-11
  minutes: 150
  cheating: true
"""
#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (50.79%)
# Likes:    1132
# Dislikes: 25
# Total Accepted:    39.6K
# Total Submissions: 75.1K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in non-decreasing order. Find the
# smallest range that includes at least one number from each of the k lists.
#
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a
# < c if b - a == d - c.
#
#
# Example 1:
#
#
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#
#
# Example 2:
#
#
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
#
#
# Example 3:
#
#
# Input: nums = [[10,10],[11,11]]
# Output: [10,11]
#
#
# Example 4:
#
#
# Input: nums = [[10],[11]]
# Output: [10,11]
#
#
# Example 5:
#
#
# Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
# Output: [1,7]
#
#
#
# Constraints:
#
#
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -10^5 <= nums[i][j] <= 10^5
# nums[i] is sorted in non-decreasing order.
#
#
#

# @lc code=start

from typing import List, Tuple
import heapq
from collections import namedtuple


def simplify(nums: List[int]):
    s = set()
    out = []
    for n in nums:
        if n in s:
            pass
        else:
            s.add(n)
            out.append(n)
    return out


End = namedtuple("End", ["num", "num_index", "list_index"])

def smaller_range(range1: Tuple[int, int], range2: Tuple[int, int]) -> Tuple[int, int]:
    a, b = range1
    c, d = range2
    if b - a < d - c:
        return range1
    if b - a > d - c:
        return range2
    if a < c:
        return range1
    else:
        return range2


class Solution:
    def smallestRange(self, lists: List[List[int]]) -> List[int]:
        # for i in range(len(lists)):
        #     lists[i] = simplify(lists[i])

        heap: List[End] = []
        max_in_heap: int = -1 * 10 ** 5
        for i, li in enumerate(lists):
            heapq.heappush(heap, End(num=li[0], num_index=0, list_index=i))
            max_in_heap = max(max_in_heap, li[0])

        best_range = (heap[0].num, max_in_heap)

        while True:
            # print("heap:", heap)
            # print("best_range:", best_range)

            end = heapq.heappop(heap)
            li = lists[end.list_index]
            if end.num_index + 1 < len(li):
                heapq.heappush(heap, End(num=li[end.num_index + 1], num_index=end.num_index + 1, list_index=end.list_index,))
                max_in_heap = max(max_in_heap, li[end.num_index + 1])
                best_range = smaller_range(best_range, (heap[0].num, max_in_heap))
            else:
                break
        return list(best_range)


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().smallestRange
    t.assertEqual(f([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]), [20, 24])
    t.assertEqual(f([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), [1, 1])
    t.assertEqual(f([[1], [2], [3], [4], [5], [6], [7]]), [1, 7])
