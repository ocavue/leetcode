"""
submits:
- date: 2021-01-20
  minutes: 69
  cheating: true
labels:
- dp
comment: |
  这道题评论特别搞笑，一帮人说太难了，还有一些人说这就是教科书般的 DP，是 Matrix chain multiplication 的变种
  https://en.wikipedia.org/wiki/Matrix_chain_multiplication
"""
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (52.46%)
# Likes:    3281
# Dislikes: 92
# Total Accepted:    125.9K
# Total Submissions: 234.7K
# Testcase Example:  '[3,1,5,8]'
#
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted
# with a number on it represented by an array nums. You are asked to burst all
# the balloons.
#
# If you burst the i^th balloon, you will get nums[i - 1] * nums[i] * nums[i +
# 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as
# if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
#
# Example 1:
#
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# Example 2:
#
#
# Input: nums = [1,5]
# Output: 10
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100
#
#
#

from typing import List

# @lc code=start


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        # dp[i][j] 表示 「 射爆 nums[i:j] 中所有气球，而且 nums[i-1] 以及 nums[j] 这两个气球都没有被射爆时 」 所能取得的最高分数
        dp = [[-1] * len(nums) for _ in range(len(nums))]

        for m in range(0, len(nums) - 1):
            for j in range(m + 1, len(nums)):
                i = j - m

                best = 0
                for k in range(i, j):
                    best = max(best, dp[i][k] + nums[i - 1] * nums[k] * nums[j] + dp[k + 1][j])
                dp[i][j] = best

        return dp[1][len(nums) - 1]


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().maxCoins)

    t([[3, 1, 5, 8]], 167)
    t([[1, 5]], 10)
