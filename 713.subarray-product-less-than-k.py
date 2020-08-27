"""
submits:
- date: 2020-08-27
  minutes: 27
  cheating: false
labels:
- two-pointers
"""
#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (38.43%)
# Likes:    1419
# Dislikes: 62
# Total Accepted:    62.7K
# Total Submissions: 160.1K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all
# the elements in the subarray is less than k.
#
# Example 1:
#
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
# [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
#
#
#
# Note:
# 0 < nums.length .
# 0 < nums[i] < 1000.
# 0 .
#
#

# @lc code=start

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        # p = nums[i] * nums[i+1] * ... * nums[j-1]
        i, j, p = 0, 1, nums[0]

        count = 0
        while j <= len(nums):
            assert 0 <= i < j <= len(nums)

            if p < k:
                count += j - i
                p *= nums[j] if j < len(nums) else 1
                j += 1
            else:
                if i + 1 < j:
                    p //= nums[i]
                    i += 1
                else:
                    p *= nums[j] if j < len(nums) else 1
                    j += 1

            assert 0 <= i < j <= len(nums) + 1
        return count


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().numSubarrayProductLessThanK
    t.assertEqual(f([10, 5, 2, 6], 100), 8)
