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


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length_of_lts_endswith_k_list = []

        for k in range(0, len(nums)):
            if k == 0:
                length_of_lts_endswith_k_list.append(1)
            else:
                length_of_lts_endswith_k = 1
                for i in range(0, k):
                    if nums[i] < nums[k]:
                        length_of_lts_endswith_k = max(
                            length_of_lts_endswith_k,
                            length_of_lts_endswith_k_list[i] + 1,
                        )
                length_of_lts_endswith_k_list.append(length_of_lts_endswith_k)
            assert len(length_of_lts_endswith_k_list) == k + 1

        return (
            max(length_of_lts_endswith_k_list) if length_of_lts_endswith_k_list else 0
        )


# @lc code=end
