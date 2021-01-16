"""
submits:
- date: 2021-01-16
  minutes: 59
  cheating: false
labels:
- dp
"""
#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (39.00%)
# Likes:    3106
# Dislikes: 82
# Total Accepted:    269.7K
# Total Submissions: 679.8K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
#
# Example 2:
#
#
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are engaging multiple transactions at the same time. You must sell before
# buying again.
#
#
# Example 3:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
# Example 4:
#
#
# Input: prices = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5
#
#
#

from typing import List

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def cache(cal):
            dp = [
                None,
                [-1] * len(prices),
                [-1] * len(prices),
                [-1] * len(prices),
                [-1] * len(prices),
            ]

            def new_cal(day, transactions):
                if not transactions:
                    return 0

                if dp[transactions][day] == -1:
                    dp[transactions][day] = cal(day, transactions)
                return dp[transactions][day]

            return new_cal

        @cache
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
            for transaction in [1, 2, 3, 4]:
                cal(day, transaction)

        return cal(0, 4)


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().maxProfit)

    t([[3, 3, 5, 0, 0, 3, 1, 4]], 6)
    t([[1, 2, 3, 4, 5]], 4)
    t([[7, 6, 4, 3, 1]], 0)
    t([[1]], 0)

