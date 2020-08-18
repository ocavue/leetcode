"""
submits:
- date: 2020-08-18
  minutes: 47
  cheating: false
"""
#
# @lc app=leetcode id=768 lang=python3
#
# [768] Max Chunks To Make Sorted II
#
# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/
#
# algorithms
# Hard (47.83%)
# Likes:    438
# Dislikes: 19
# Total Accepted:    21.4K
# Total Submissions: 43.9K
# Testcase Example:  '[5,4,3,2,1]'
#
# This question is the same as "Max Chunks to Make Sorted" except the integers
# of the given array are not necessarily distinct, the input array could be up
# to length 2000, and the elements could be up to 10**8.
#
#
#
# Given an array arr of integers (not necessarily distinct), we split the array
# into some number of "chunks" (partitions), and individually sort each chunk.
# After concatenating them, the result equals the sorted array.
#
# What is the most number of chunks we could have made?
#
# Example 1:
#
#
# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
# which isn't sorted.
#
#
# Example 2:
#
#
# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks
# possible.
#
#
# Note:
#
#
# arr will have length in range [1, 2000].
# arr[i] will be an integer in range [0, 10**8].
#
#
#
#
#

# @lc code=start

from typing import List


class Chunk:
    def __init__(self, num: int):
        self.min = num
        self.max = num

    def add_num(self, num: int):
        if self.min > num:
            self.min = num
        if self.max < num:
            self.max = num


def merge_chunks(left: Chunk, right: Chunk):
    assert not is_valid_neighbor(left, right)

    left.min = min(left.min, right.min)
    left.max = max(left.max, right.max)
    return left


def is_valid_neighbor(left: Chunk, right: Chunk):
    return left.max <= right.min


def normalize_chunks(chunks: List[Chunk]):
    while len(chunks) >= 2:
        curr_chunk = chunks[-1]
        prev_chunk = chunks[-2]
        if is_valid_neighbor(prev_chunk, curr_chunk):
            break
        else:
            chunks[-2] = merge_chunks(prev_chunk, curr_chunk)
            chunks.pop()

    # for i in range(len(chunks) - 1):
    #     left, right = chunks[i], chunks[i + 1]
    #     assert is_valid_neighbor(left, right)


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks: List[Chunk] = []
        for num in arr:
            if len(chunks) == 0:
                chunks.append(Chunk(num))
            else:
                chunks.append(Chunk(num))
                normalize_chunks(chunks)
        return len(chunks)


# @lc code=end
if __name__ == "__main__":
    f = Solution().maxChunksToSorted
    import unittest

    t = unittest.TestCase("__init__")
    t.assertEqual(f([2, 1, 3, 4, 4]), 4)
    t.assertEqual(f([5, 4, 3, 2, 1]), 1)
    t.assertEqual(f([0, 0, 0, 1, 1]), 5)
