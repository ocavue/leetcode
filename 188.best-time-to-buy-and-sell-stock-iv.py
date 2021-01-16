"""
submits:
- date: 2021-01-16
  minutes: 4
  cheating: False
labels:
- dp
commnet: 从 123 题抄的代码
"""
#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (28.15%)
# Likes:    2156
# Dislikes: 135
# Total Accepted:    166.9K
# Total Submissions: 569.9K
# Testcase Example:  '2\n[2,4,1]'
#
# You are given an integer array prices where prices[i] is the price of a given
# stock on the i^th day.
#
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
#
# Notice that you may not engage in multiple transactions simultaneously (i.e.,
# you must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
#
#
# Example 2:
#
#
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit
# = 3-0 = 3.
#
#
#
# Constraints:
#
#
# 0 <= k <= 100
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
#
#
#

from typing import List

# @lc code=start

from functools import lru_cache


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        @lru_cache(None)
        def cal(day: int, transactions: int) -> int:
            assert 0 <= day < len(prices)

            if transactions == 0:
                return 0

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

        # for day in range(len(prices) - 1, -1, -1):
        #     for transaction in [1, 2, 3, 4]:
        #         cal(day, transaction)

        return cal(0, 2 * k)


# @lc code=end

