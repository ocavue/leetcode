"""
submits:
- date: 2020-08-23
  cheating: true
  minutes: 35
comment: |
  这道题虽然是一道 subarray 的题目，但是不能使用双指针去实现，而是要使用「累计合」的思路去做。
  比如 [1,2,1,3] 的累计合为 [0,1,3,4,7]。然后累计合升高了 3 则说明我们找到了一个合为 3 的
  subarray
labels:
- subarray

"""
#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.47%)
# Likes:    5155
# Dislikes: 170
# Total Accepted:    347.3K
# Total Submissions: 792.3K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
#
# Constraints:
#
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
#
#
#

# @lc code=start

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        # sum_count[s] 表示满足 sum(nums[0:i]) == s 的 i 有几个
        sum_count = defaultdict(int)

        sum = 0
        sum_count[sum] = 1

        for num in nums:

            sum += num

            expected_sum = sum - k

            count += sum_count.get(expected_sum, 0)

            sum_count[sum] += 1

        return count


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().subarraySum
    t.assertEqual(f([1, 2, 1, 3], 3), 3)
    t.assertEqual(f([1, 1, 1], 2), 2)
    t.assertEqual(f([1, 2, 3], 0), 0)
    t.assertEqual(f([1], 0), 0)
