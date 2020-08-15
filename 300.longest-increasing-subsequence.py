"""
submits:
  - date: 2020-04-11
    cheating: false
  - date: 2020-08-14
    cheating: true
    minutes: 70
"""

#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.93%)
# Likes:    3909
# Dislikes: 89
# Total Accepted:    331.8K
# Total Submissions: 788.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
# Example:
#
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
# Note:
#
#
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
#

from typing import List

# @lc code=start

import bisect


def length_of_lis_v1(nums: List[int]) -> int:
    # Time: O(n*n)
    # Space: O(n)

    # length_of_lis_endswith_k_list[k] == x 表示以 nums[k] 结尾的 longest increasing subsequence 的长度。
    length_of_lis_endswith_k_list = []

    for k in range(0, len(nums)):
        if k == 0:
            length_of_lis_endswith_k_list.append(1)
        else:
            length_of_lis_endswith_k = 1
            for i in range(0, k):
                if nums[i] < nums[k]:
                    length_of_lis_endswith_k = max(length_of_lis_endswith_k, length_of_lis_endswith_k_list[i] + 1,)
            length_of_lis_endswith_k_list.append(length_of_lis_endswith_k)
        assert len(length_of_lis_endswith_k_list) == k + 1

    return max(length_of_lis_endswith_k_list) if length_of_lis_endswith_k_list else 0


def length_of_lis_v2(nums: List[int]) -> int:
    # dp[i] 表示长度为 i+1 的 Increasing Subsequence 中，末尾的数字最小是多少
    dp: List[int] = []
    for n in nums:
        # assert sorted(dp) == dp

        if len(dp) == 0:
            dp.append(n)
        else:
            if n > dp[-1]:
                dp.append(n)
            elif n == dp[-1]:
                pass
            else:
                pos = bisect.bisect_left(dp, n)
                assert dp[pos] >= n
                dp[pos] = n
        # assert sorted(dp) == dp

    # assert sorted(dp) == dp
    return len(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return length_of_lis_v2(nums)


# @lc code=end
if __name__ == "__main__":

    for input, output in [
        [[10, 9, 2, 5, 3, 7, 101, 18], 4],
        [[1, 2, 3, 4, 5], 5],
        [[5, 4, 3, 2, 1], 1],
        [[2, 2, 2, 2, 2], 1],
        [[4, 10, 4, 3, 8, 9], 3],
    ]:
        assert length_of_lis_v1(input) == output, "{} expected: {}; actual: {}".format(input, output, length_of_lis_v1(input))
        assert length_of_lis_v2(input) == output, "{} expected: {}; actual: {}".format(input, output, length_of_lis_v2(input))
