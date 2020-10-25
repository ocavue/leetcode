"""
submits:
- date: 2020-10-25
  minutes: 13
  cheating: false
labels: [dp]
"""
#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (47.68%)
# Likes:    3060
# Dislikes: 95
# Total Accepted:    169.9K
# Total Submissions: 355.9K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
#
#
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
#
#
# Example:
#
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#
#

List = list

# @lc code=start


T = True
F = False


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dps = {
            (T, T): [None] * len(prices),
            (T, F): [None] * len(prices),
            (F, T): [None] * len(prices),
            (F, F): [None] * len(prices),
        }

        def cal_with_cache(i: int, need_cooldown: bool, already_bought: bool) -> int:
            if i >= len(prices):
                return 0

            dp = dps[(need_cooldown, already_bought)]
            if dp[i] is None:
                dp[i] = cal(i, need_cooldown, already_bought)
            return dp[i]

        def cal(i: int, need_cooldown: bool, already_bought: bool) -> int:
            # do nothing
            profit = cal_with_cache(i + 1, False, already_bought)

            # buy
            if not need_cooldown and not already_bought:
                profit = max(profit, cal_with_cache(i + 1, False, True) - prices[i])
            # sell
            if already_bought:
                profit = max(profit, cal_with_cache(i + 1, True, False) + prices[i])

            return profit

        return cal_with_cache(0, False, False)


# @lc code=end
