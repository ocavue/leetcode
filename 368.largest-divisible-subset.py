"""
submits:
- date: 2020-08-25
  minutes: 36
  cheating: true
labels:
- dp
comment: |
  这道题比较有两点需要注意，第一点是「整除」本身的性质：如果我能整除整个 subset 中最大的那个数，那么我就能整除整个 subset 中的所有的数，所以我也能够加入这个 subset。第二点是如何从长度复原 subset（不复原也可以，但是耗费更多内存空间）
"""
#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (35.91%)
# Likes:    1454
# Dislikes: 71
# Total Accepted:    97.7K
# Total Submissions: 257.9K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
#
#
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
#
#
#
# Example 2:
#
#
# Input: [1,2,4,8]
# Output: [1,2,4,8]
#
#
#
#

# @lc code=start

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()

        # dp[i] 表示以 nums[i] 为最大值的 subset 的最长长度是多少
        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            best_len = 1
            for j in range(0, i):
                if num % nums[j] == 0:
                    best_len = max(best_len, dp[j] + 1)
            dp[i] = best_len

        max_index, max_len = 0, dp[0]
        for i in range(1, len(nums)):
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        max_num = nums[max_index]

        # 复原 subset
        subset = [max_num]
        expected_len = max_len - 1
        for i in range(max_index, -1, -1):

            # subset[-1] 是当前 subset 中最小的数字
            # 如果 subset[-1] 能够整除 nums[i]，那么说明
            # subset 中每个元素都能整除 nums[i]
            if subset[-1] % nums[i] == 0 and dp[i] == expected_len:
                subset.append(nums[i])
                expected_len -= 1
        return subset


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().largestDivisibleSubset
    t.assertEqual(set(f([1, 2, 3])), set([1, 2]))
    t.assertEqual(set(f([1, 2, 4, 8])), set([1, 2, 4, 8]))

