"""
submits:
  - date: 2020-07-07
    cheating: false
"""

#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (42.37%)
# Likes:    2553
# Dislikes: 70
# Total Accepted:    176.6K
# Total Submissions: 407.1K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
#
# Note:
#
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
#
#
# Example 1:
#
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
#
#
# Example 2:
#
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
#
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        num_sum = sum(nums)
        if num_sum % 2 == 1:
            return False
        half_sum = num_sum // 2

        cache_map = []
        for i in range(len(nums)):
            cache_map.append([None for j in range(half_sum + 1)])

        def can_sum(max_index: int, target_sum: int) -> bool:
            assert 0 <= max_index < len(nums)

            if cache_map[max_index][target_sum] is True:
                return True
            if cache_map[max_index][target_sum] is False:
                return False

            if target_sum < 0:
                cache_map[max_index][target_sum] = False
                return False

            if max_index == 0:
                if nums[0] == target_sum:
                    cache_map[max_index][target_sum] = True
                    return True
                else:
                    cache_map[max_index][target_sum] = False
                    return False

            else:
                # 看看如果不包含属于 max_index 的数字是不是能凑成 target_sum
                if can_sum(max_index - 1, target_sum=target_sum):
                    cache_map[max_index][target_sum] = True
                    return True
                # 看看如果包含属于 max_index 的数字是不是能凑成 target_sum
                if can_sum(max_index - 1, target_sum=target_sum - nums[max_index]):
                    cache_map[max_index][target_sum] = True
                    return True
                cache_map[max_index][target_sum] = False
                return False

        return can_sum(len(nums) - 1, half_sum)


# @lc code=end
if __name__ == "__main__":
    t = Solution().canPartition

    assert t([1, 5, 11, 5]) is True
    assert t([1, 2, 3, 5]) is False
    assert t([2, 2, 3, 5]) is False
    assert (
        t(
            [
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
            ]
        )
        is True
    )

