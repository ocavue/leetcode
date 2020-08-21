"""
submits:
- date: 2020-08-20
  minutes: 10
  cheating: false
labels:
- max/min elements in sliding window

"""
#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#
# https://leetcode.com/problems/online-stock-span/description/
#
# algorithms
# Medium (53.20%)
# Likes:    958
# Dislikes: 134
# Total Accepted:    71.2K
# Total Submissions: 118.2K
# Testcase Example:  '["StockSpanner","next","next","next","next","next","next","next"]\n' +  '[[],[100],[80],[60],[70],[60],[75],[85]]'
#
# Write a class StockSpanner which collects daily price quotes for some stock,
# and returns the span of that stock's price for the current day.
#
# The span of the stock's price today is defined as the maximum number of
# consecutive days (starting from today and going backwards) for which the
# price of the stock was less than or equal to today's price.
#
# For example, if the price of a stock over the next 7 days were [100, 80, 60,
# 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
#
#
#
#
# Example 1:
#
#
# Input: ["StockSpanner","next","next","next","next","next","next","next"],
# [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation:
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.
#
# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's
# price.
#
#
#
#
# Note:
#
#
# Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# There will be at most 10000 calls to StockSpanner.next per test case.
# There will be at most 150000 calls to StockSpanner.next across all test
# cases.
# The total time limit for this problem has been reduced by 75% for C++, and
# 50% for all other languages.
#
#
#
#

# @lc code=start

from typing import List, Tuple


class StockSpanner:
    def __init__(self):
        self.stack: List[Tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack:
            last_price, last_span = self.stack[-1]
            if last_price <= price:
                span += last_span
                self.stack.pop()
            else:
                break
        self.stack.append((price, span))

        # assert sorted(self.stack, reverse=True) == self.stack
        # print("next for", price, "is", span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
if __name__ == "__main__":
    s = StockSpanner()
    assert s.next(100) == 1
    assert s.next(80) == 1
    assert s.next(60) == 1
    assert s.next(70) == 2
    assert s.next(60) == 1
    assert s.next(75) == 4
    assert s.next(85) == 6
