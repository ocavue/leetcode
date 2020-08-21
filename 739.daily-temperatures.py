"""
submits:
- minutes: 20
  cheating: false
  date: 2020-08-19

labels:
- max/min elements in sliding window

"""
#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (62.00%)
# Likes:    3034
# Dislikes: 91
# Total Accepted:    171.2K
# Total Submissions: 270.1K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
#
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
#
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#
#

# @lc code=start

from typing import List, Tuple

T = int


class Solution:
    def dailyTemperatures(self, temps: List[T]) -> List[T]:

        """
        stack 中储存着所有没有找到更温暖日子的 index

        按照温度，stack 中的值是严格单调递减的。
        按照index，stack 中的值是严格单调递增的。
        """
        stack: List[Tuple[int, T]] = list()

        result = [0] * len(temps)

        for index, temp in enumerate(temps):

            while stack:
                last_index, last_temp = stack[-1]
                if last_temp < temp:
                    stack.pop()
                    result[last_index] = index - last_index
                else:
                    break

            stack.append((index, temp))

        return result


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    f = Solution().dailyTemperatures

    t.assertEqual(f([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
