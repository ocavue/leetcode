"""
submits:
  - date: 2020-04-11
    cheating: false
  - date: 2020-08-14
    cheating: true
    minutes: 70
  - date: 2020-09-16
    cheating: false
    minutes: 27
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


def length_of_lis_v2(nums: List[int]) -> int:

    # dp[i] = num 表示所有长度为 i+1 的 increasing subsequence 中，末尾数字最小的那个 increasing subsequence 的末尾数字。
    dp = [nums[0]]

    for num in nums:
        i = bisect.bisect_left(dp, num)
        dp[i : i + 1] = [num]

    # print(dp)
    return len(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
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
        # assert length_of_lis_v1(input) == output, "{} expected: {}; actual: {}".format(input, output, length_of_lis_v1(input))
        assert length_of_lis_v2(input) == output, "{} expected: {}; actual: {}".format(input, output, length_of_lis_v2(input))
