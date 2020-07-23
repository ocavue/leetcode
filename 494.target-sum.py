"""
submits:
  - date: 2020-07-23
    cheating: false
    minutes: 72
labels: [dp]
comment: |
  这道题也需要使用动态规划。动态规划本身的思路是没问题的，但是在做题的时候一些边缘的 index 计算上翻了很多错。以后还是从一开始写成小函数好了，不要相信自己的指针运算。
"""
#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (46.44%)
# Likes:    2632
# Dislikes: 110
# Total Accepted:    168K
# Total Submissions: 361.7K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.
#
# Example 1:
#
#
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
#
#
#
# Constraints:
#
#
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
#
#
#

from typing import List
from pprint import pprint

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target_sum: int) -> int:
        """
        >>> f = Solution().findTargetSumWays
        >>> f([1,1,1,1,1], 3)
        5
        >>> f([1], 2)
        0
        >>> f([1], 1)
        1
        >>> f([1,0], 1)
        2

        """

        if not nums:
            return 0

        # dp 表示在使用前 x 个数字的情况下，合为 y 的组合的数量是 z
        # 其中
        #       1 <= x <= len(nums)
        #       -sum(nums) <= y <= sum(nums)
        #       z >= 0
        # dp[x][y] = z
        dp: List[List[int]] = []
        max_sum = sum(nums)

        # 下面几种明显的情况优先处理，防止等下数组越界
        if target_sum > +max_sum:
            return 0
        if target_sum < -max_sum:
            return 0

        # 定义 dp 的 setter 和 getter。稍微降低性能，但是让逻辑更清晰
        def get_ways(num_count: int, sum: int):
            # assert 0 <= num_count <= len(nums), f"num_count {num_count} is invaild"
            # assert -max_sum <= sum <= max_sum

            return dp[num_count][sum + max_sum]

        def add_ways(num_count: int, sum: int, add_way_count: int):
            # assert 0 <= num_count <= len(nums), f"num_count {num_count} is invaild"
            # assert -max_sum <= sum <= max_sum
            # assert add_way_count >= 0

            dp[num_count][sum + max_sum] += add_way_count

        # 初始化 dp
        for x in range(len(nums) + 1):
            dp.append([0] * (max_sum * 2 + 1))
        add_ways(0, 0, 1)  # 当使用 0 个数字时，凑出合为 0 的方式有且仅有 1 种，就是使用 0 个数字（听起来像是绕口令）

        for num_index, num in enumerate(nums):
            num_count = num_index + 1

            for pre_sum in range(-max_sum, max_sum + 1):
                pre_ways = get_ways(num_count - 1, pre_sum)
                if pre_ways:
                    add_ways(num_count, pre_sum + num, pre_ways)
                    add_ways(num_count, pre_sum - num, pre_ways)

        # pprint(dp)

        return get_ways(len(nums), target_sum)


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
