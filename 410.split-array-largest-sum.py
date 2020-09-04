"""
submits:
- date: 2020-09-04
  minutes: 120
  cheating: true
labels:
- bisect
"""
# 44
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (43.63%)
# Likes:    1968
# Dislikes: 77
# Total Accepted:    97.6K
# Total Submissions: 217.7K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array nums which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
#
# Write an algorithm to minimize the largest sum among these m subarrays.
#
#
# Example 1:
#
#
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
#
#
# Example 3:
#
#
# Input: nums = [1,4,4], m = 3
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= m <= min(50, nums.length)
#
#
#

# @lc code=start

from typing import List


# 使用 dp，
# n = len(nums)
# 空间：O(n*m)
# 时间：O(n*m*n)
def split_array_v1(self, nums: List[int], m: int) -> int:

    # dp[i][x] 表示把 nums[i:] 拆成 x 份，那 largest_sum 是多少
    # 其中 0<=i<len(nums)
    #     1<=x<=m
    dp: List[List[int]] = []
    for _ in range(len(nums)):
        dp.append([-1] * (m + 1))

    # sums[i] = sum(nums[i:])
    sums = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        if i == len(nums) - 1:
            sums[i] = num
        else:
            sums[i] = num + sums[i + 1]

    def cal_sum(i: int, j: int):
        # 计算 sum(nums[i:j])
        assert 0 <= i <= j < len(nums)
        # assert sums[i] - sums[j] == sum(nums[i:j]), f"nums: {nums}; sums: {sums}"  # TODO: delete this
        return sums[i] - sums[j]

    def cal_dp(i: int, x: int):
        assert 0 <= i < len(nums)
        assert 1 <= x <= m

        # if (i, x) == (0, 2):
        #     print("x")

        if dp[i][x] == -1:
            if x == 1:
                dp[i][x] = sums[i]
            else:
                best_sum = sums[0] + 1
                for j in range(i + 1, len(nums)):
                    print("j", j)

                    best_sum = min(best_sum, max(cal_sum(i, j), dp[j][x - 1]))
                    # 随着 j 的升高，cal_sum(i, j) 递增，dp[j][x - 1]) 递减，所以在某个时刻就不用看了
                    if cal_sum(i, j) > dp[j][x - 1]:
                        break
                dp[i][x] = best_sum
        return dp[i][x]

    for x in range(1, m + 1):
        for i in range(len(nums) - 1, -1, -1):
            cal_dp(i, x)

    return cal_dp(i, x)


def split_array(nums: List[int], max_sum: int) -> int:

    curr_sum = 0
    count = 0
    for i in nums:
        curr_sum += i
        if curr_sum > max_sum:
            count += 1
            curr_sum = i

    # print(nums, max_sum, count+1)
    return count + 1


def is_ok(nums: List[int], max_sum: int, m: int) -> bool:
    return split_array(nums, max_sum) <= m


def split_array_v2(nums: List[int], m: int) -> int:
    lo = max(nums)
    hi = sum(nums) + 1

    while lo < hi:
        mi = (hi + lo) // 2

        chunks = split_array(nums, mi)

        if chunks < m:
            hi = mi
        elif chunks > m:
            lo = mi + 1
        elif chunks == m:
            hi = mi

    return lo


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return split_array_v2(nums, m)


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = split_array_v2
    t.assertEqual(f(nums=[7, 2, 5, 10, 8], m=2), 18)
    t.assertEqual(f(nums=[1, 2, 3, 4, 5], m=2), 9)
    t.assertEqual(f(nums=[1, 4, 4], m=3), 4)
    t.assertEqual(
        f(
            # fmt:off
            nums=[
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,150,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,250,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,300,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,350,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,400,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,450,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,500,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,550,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,600,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,650,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,700,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,750,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,800,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,850,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,900,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,950,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            ],
            m=50,
        ),
        950,
    )
