"""
submits:
- date: 2020-08-28
  cheating: false
  minutes: 60
comment: |
  这道题有点意思，但是我还不知道背后的套路
"""
#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#
# https://leetcode.com/problems/patching-array/description/
#
# algorithms
# Hard (34.08%)
# Likes:    520
# Dislikes: 73
# Total Accepted:    36.9K
# Total Submissions: 106.8K
# Testcase Example:  '[1,3]\n6'
#
# Given a sorted positive integer array nums and an integer n, add/patch
# elements to the array such that any number in range [1, n] inclusive can be
# formed by the sum of some elements in the array. Return the minimum number of
# patches required.
#
# Example 1:
#
#
# Input: nums = [1,3], n = 6
# Output: 1
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3,
# 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
# [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
#
# Example 2:
#
#
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].
#
#
# Example 3:
#
#
# Input: nums = [1,2,2], n = 5
# Output: 0
#
#

# @lc code=start

from typing import List, Set


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 我们观察 nums[0:k] 项加上新加的数字是否能凑够 1...m 中的每一个数字
        # 其中
        # 0 <= k <= len(nums)
        # 1 <= m <= n

        if len(nums) >= 1 and nums[0] == 1:
            k, m = 1, 1
            count = 0
        else:
            k = 0
            m = 1
            count = 1

        while m < n:
            # 遍历到这一行的时候，使用 nums[0:k] 加上 count 个数字，可以凑够 1...m 中的每一个数字

            if k < len(nums) and nums[k] <= m + 1:
                # 再算上 nums[k]，我们可以凑够 m+1 ... m+nums[k] 个数字，也就是我们能够凑出 1...m+num[k] 中的每一个数字
                m += nums[k]
                k += 1
            else:
                # 再算上 nums[k]，我们也凑不出 m+1。所以我们加入一个新的数字：m+1
                count += 1
                m += m + 1

        return count

# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().minPatches
    t.assertEqual(f([1, 3], 6), 1)
    t.assertEqual(f([1, 5, 10], 20), 2)
    t.assertEqual(f([1, 2, 2], 5), 0)
