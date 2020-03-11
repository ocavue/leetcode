#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (59.96%)
# Likes:    4210
# Dislikes: 233
# Total Accepted:    477.1K
# Total Submissions: 795.6K
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#

from typing import List

# @lc code=start


class Solution:
    def _add_result(
        self, results: List[str], left_open: int, left_close: int
    ) -> List[str]:
        # assert left_close >= left_open
        # assert left_open >= 0
        # assert left_close >= 0

        if left_open >= 1 or left_close >= 1:
            new_results = []

            if left_open >= 1:
                new_results += self._add_result(
                    [i + "(" for i in results], left_open - 1, left_close
                )

            if left_close >= 1 and left_close > left_open:
                new_results += self._add_result(
                    [i + ")" for i in results], left_open, left_close - 1
                )

            return new_results
        else:
            return results

    def generateParenthesis(self, n: int) -> List[str]:
        if n > 0:
            return self._add_result(["("], n - 1, n)
        else:
            return []


# @lc code=end

if __name__ == "__main__":
    print(Solution().generateParenthesis(4))
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(0))
