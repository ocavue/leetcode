"""
submits:
- date: 2020-01-08
  cheating: true
  minutes: 45
"""
#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (35.92%)
# Likes:    2009
# Dislikes: 112
# Total Accepted:    72.5K
# Total Submissions: 189.2K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an integer array nums, return the number of longest increasing
# subsequences.
#
# Notice that the sequence has to be strictly increasing.
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1,
# 3, 5, 7].
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
#
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6
#
#
#

from typing import List

# @lc code=start


class Solution:
    def findNumberOfLIS(self, values: List[int]) -> int:
        # For a sequence of numbers,
        #
        #

        l = [1] * len(values)  # l[k] is the length of longest subsequence ending with values[k];
        c = [0] * len(values)  # c[k] is total number of longest subsequence ending with values[k];

        res = 0
        max_len = 0
        for i in range(len(values)):
            l[i] = 1
            for j in range(0, i):
                if values[j] < values[i]:
                    l[i] = max(l[i], l[j] + 1)
            max_len = max(max_len, l[i])
        for i in range(len(values)):
            if l[i] == 1:
                c[i] = 1
            else:
                c[i] = 0
                for j in range(0, i):
                    if values[j] < values[i] and l[j] == l[i] - 1:
                        c[i] += c[j]
            if l[i] == max_len:
                res += c[i]

        return res


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().findNumberOfLIS
    t(f([1, 3, 5, 4, 7]), 2)
    t(f([2, 2, 2, 2, 2]), 5)
