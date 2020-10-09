"""
submits:
- date: 2020-10-09
  cheating: true
  minutes: 37
comment: |
  这道题可以看作是某种 merge K sorted list

    ugly number                       K sorted list
        1                            2     7    13   19     1 * [2,7,13,19]
        |                            |     |    |    |
        2                            4     14   26   38     2 * [2,7,13,19]
        |                            |     |    |    |
        4                            8     28   52   76     4 * [2,7,13,19]
        |                            |     |    |    |
        7                            14    49   91   133    7 * [2,7,13,19]
        |                            |     |    |    |
        8                            16    56   ...   ...   8 * [2,7,13,19]
        |                            |     |    |     |
        .                            .     .     .    .
        .                            .     .     .    .
        .                            .     .     .    .
    虽然 ugly number 的争夺，K sorted list 中的每个 sorted list 都在增长。我们要在这 K 个 sorted list 中找到最小的那个数字
"""
#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (43.77%)
# Likes:    696
# Dislikes: 149
# Total Accepted:    80.7K
# Total Submissions: 177.7K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the n^th super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
#
# Example:
#
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12
# ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
#
# Note:
#
#
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000.
# The n^th super ugly number is guaranteed to fit in a 32-bit signed integer.
#
#
#

# @lc code=start

import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        K = len(primes)
        ugly_nums = [1]
        k_idxs = [0] * K # k_idxs[k]=i 表示第 k 个 sorted list 的下一个数字是在 index 为 i 的位置。其中 0 <= k < K, i >= i

        heap = []
        for k in range(K):
            heapq.heappush(heap, (ugly_nums[k_idxs[k]] * primes[k], k))

        while len(ugly_nums) < n:
            next_ugly_num, k = heapq.heappop(heap)

            # 有可能出现重复的情况
            if next_ugly_num != ugly_nums[-1]:
                ugly_nums.append(next_ugly_num)

            k_idxs[k] += 1
            heapq.heappush(heap, (ugly_nums[k_idxs[k]] * primes[k], k))

        return ugly_nums[-1]

# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().nthSuperUglyNumber
    t.assertEqual(
        f(n=12, primes=[2, 7, 13, 19]), 32,
    )
