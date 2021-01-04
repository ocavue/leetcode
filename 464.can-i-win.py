
"""
submits:
- minutes: 66
  cheating: true
  date: 2020-01-04
labels:
- dp
commnet: |
  这道题我没有注意到的一点是：如果 choosable 定下来了，那么 reminder 可以推导出来的。所以 dp 使用 choosable 作为 key 就可以了，不需要再将 reminder 组合进来。
"""
#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (29.37%)
# Likes:    1162
# Dislikes: 194
# Total Accepted:    58K
# Total Submissions: 196.5K
# Testcase Example:  '10\n11'
#
# In the "100 game" two players take turns adding, to a running total, any
# integer from 1 to 10. The player who first causes the running total to reach
# or exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of
# numbers from 1 to 15 without replacement until they reach a total >= 100.
#
# Given two integers maxChoosableInteger and desiredTotal, return true if the
# first player to move can force a win, otherwise return false. Assume both
# players play optimally.
#
#
# Example 1:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 11
# Output: false
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
#
#
# Example 2:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 0
# Output: true
#
#
# Example 3:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 1
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= maxChoosableInteger <= 20
# 0 <= desiredTotal <= 300
#
#
#

# @lc code=start


from functools import lru_cache


def can_i_win(choosable: int, remainder: int, dp: dict) -> bool:
    if choosable in dp:
        return dp[choosable]

    assert choosable >= 0
    assert remainder >= 0
    for i in range(21):
        if 1 & (choosable >> i):
            value = i + 1
            if value >= remainder:
                dp[choosable] = True
                return True
            else:
                next_choosable = choosable - (1 << i)
                assert 1 & (next_choosable >> i) == 0
                if not can_i_win(next_choosable, remainder - value, dp):
                    dp[choosable] = True
                    return True
    dp[choosable] = False
    return False


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if sum(list(range(1, maxChoosableInteger + 1))) < desiredTotal:
            return False
        return can_i_win((1 << (maxChoosableInteger)) - 1, desiredTotal, {})


# @lc code=end
if __name__ == "__main__":
    f = Solution().canIWin
    from tool import t

    t(f(10, 11), False)
    t(f(10, 0), True)
    t(f(10, 1), True)
    t(f(19, 79), True)
    t(f(18, 79), True)
