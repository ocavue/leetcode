"""
submits:
- date: 2020-09-11
  cheating: true
  minutes: 120
labels: [dp]
"""
#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#
# https://leetcode.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (26.35%)
# Likes:    971
# Dislikes: 86
# Total Accepted:    21.6K
# Total Submissions: 79.9K
# Testcase Example:  '1\n2'
#
# You are given K eggs, and you have access to a building with N floors from 1
# to N.
#
# Each egg is identical in function, and if an egg breaks, you cannot drop it
# again.
#
# You know that there exists a floor F with 0 <= F <= N such that any egg
# dropped at a floor higher than F will break, and any egg dropped at or below
# floor F will not break.
#
# Each move, you may take an egg (if you have an unbroken one) and drop it from
# any floor X (with 1 <= X <= N).
#
# Your goal is to know with certainty what the value of F is.
#
# What is the minimum number of moves that you need to know with certainty what
# F is, regardless of the initial value of F?
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: K = 1, N = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty
# that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with
# certainty.
#
#
#
# Example 2:
#
#
# Input: K = 2, N = 6
# Output: 3
#
#
#
# Example 3:
#
#
# Input: K = 3, N = 14
# Output: 4
#
#
#
#
# Note:
#
#
# 1 <= K <= 100
# 1 <= N <= 10000
#
#
#
#
#
#

# @lc code=start

from functools import lru_cache
from typing import List


# 当你有 n 个地方可以敲击时
def egg_drop(k: int, n: int, best_i: int, dp: List[List[int]]) -> tuple:
    assert k >= 1
    # assert n >= 0

    if n <= 0:
        return 0, 0
    if n == 1:
        return 1, 0
    if n == 2:
        return 2, 0
    if k == 1:
        return n, 0

    best_wrost_times = 20000
    for i in range(best_i, n + 1):
        # i break
        case1 = dp[k - 1][i - 1]  # 随着 i 升高，单调递增
        # i not break
        case2 = dp[k][n - i]  # 随着 i 升高，单调递减

        wrost_times = 1 + max(case1, case2)
        if wrost_times<best_wrost_times :
            best_wrost_times = wrost_times
            best_i = i
        elif wrost_times > best_wrost_times:
            break
    return best_wrost_times, best_i


class Solution:
    def superEggDrop_v1(self, K: int, N: int) -> int:
        # dp[k][n] 表示 egg_drop(k, n) 的返回值
        dp = []
        for k in range(0, K + 1):
            dp.append([-1] * (N + 1))
        for k in range(1, K + 1):
            best_i = 0
            for n in range(0, N + 1):
                dp[k][n], best_i = egg_drop(k, n, best_i, dp)

        return dp[K][N]

    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N: return m

# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().superEggDrop

    t.assertEqual(f(K=1, N=2), 2)
    t.assertEqual(f(K=1, N=1), 1)
    t.assertEqual(f(K=2, N=6), 3)
    t.assertEqual(f(K=3, N=14), 4)
    t.assertEqual(f(K=2, N=2), 2)
    t.assertEqual(f(K=2, N=1), 1)
    t.assertEqual(f(K=2, N=4), 3)
    t.assertEqual(f(K=10, N=100), 7)
    t.assertEqual(f(K=4, N=5000), 19)
