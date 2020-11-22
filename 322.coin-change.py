"""
submits:
 - date: 2020-07-07
   cheating: false
 - date: 2020-11-22
   cheating: false
   minutes: 3
labels: [dp]
"""
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (36.16%)
# Likes:    5403
# Dislikes: 164
# Total Accepted:    507.9K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
# Example 4:
#
#
# Input: coins = [1], amount = 1
# Output: 1
#
#
# Example 5:
#
#
# Input: coins = [1], amount = 2
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], targetAmount: int) -> int:
        if targetAmount == 0:
            return 0

        # index 是硬币的金额之和
        # value 是凑出这个金额所需要的最少的硬币数量
        amountMap = [0] * (targetAmount + 1)

        for amount in range(1, targetAmount + 1):
            for coin in coins:
                if coin == amount:
                    amountMap[amount] = 1
                    break
                if amount - coin > 0:
                    rest = amountMap[amount - coin]
                    if rest != 0:
                        if amountMap[amount] == 0:
                            amountMap[amount] = rest + 1
                        else:
                            amountMap[amount] = min(rest + 1, amountMap[amount])
        if amountMap[targetAmount] == 0:
            return -1
        return amountMap[targetAmount]


# @lc code=end

