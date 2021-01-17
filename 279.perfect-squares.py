"""

submits:
- date: 2021-01-17
  minutes: 10
  cheating: false
labels:
- dp
"""
# 2053
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (47.96%)
# Likes:    3827
# Dislikes: 225
# Total Accepted:    366.8K
# Total Submissions: 754.5K
# Testcase Example:  '12'
#
# Given an integer n, return the least number of perfect square numbers that
# sum to n.
#
# A perfect square is an integer that is the square of an integer; in other
# words, it is the product of some integer with itself. For example, 1, 4, 9,
# and 16 are perfect squares while 3 and 11 are not.
#
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc code=start

from functools import lru_cache


@lru_cache(None)
def numSquares(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    best = n
    m = int(n ** 0.5)
    for i in range(m, 0, -1):
        best = min(best, 1 + numSquares(n - i * i))
    return best


class Solution:
    def numSquares(self, n: int) -> int:
        return numSquares(n)


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().numSquares)
    t([12], 3)
    t([13], 2)

