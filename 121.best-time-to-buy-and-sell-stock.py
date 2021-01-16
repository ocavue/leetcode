"""
submits:
- date: 2021-01-16
  minutes: 50
  cheating: false
lables:
- dp
"""
#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.01%)
# Likes:    7260
# Dislikes: 321
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#
#
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
#
#
# Example 2:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
#
#

from typing import List

# @lc code=start

# from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def lru_cache(cal):
            dp = {
                1: [-1] * len(prices),
                2: [-1] * len(prices),
            }

            def new_cal(day, transactions):
                if not transactions:
                    return 0

                if dp[transactions][day] == -1:
                    dp[transactions][day] = cal(day, transactions)
                return dp[transactions][day]

            return new_cal

        @lru_cache
        def cal(day: int, transactions: int) -> int:
            assert 0 <= day < len(prices)
            has_stock = transactions % 2 == 1
            if day == len(prices) - 1:
                if has_stock:
                    return prices[day]
                else:
                    return 0

            if has_stock:
                # sale
                case1 = cal(day + 1, transactions - 1) + prices[day]
                # not sale
                case2 = cal(day + 1, transactions)
                return max(case1, case2)
            else:
                # buy
                case1 = cal(day + 1, transactions - 1) - prices[day]
                # not buy
                case2 = cal(day + 1, transactions)
                return max(case1, case2)

        for day in range(len(prices) - 1, -1, -1):
            for transaction in [2, 1]:
                cal(day, transaction)

        return cal(0, 2)


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().maxProfit)
    t([[7, 1, 5, 3, 6, 4]], 5)
